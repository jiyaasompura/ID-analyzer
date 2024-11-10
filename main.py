from flask import Flask
from verification import Verify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
import requests
import json
import os

# Initialize Flask application
app = Flask("__main__")

# Initialize verification instance
verify = Verify()

# Database configuration and model setup
class Base(DeclarativeBase):
    """Base class for SQLAlchemy ORM"""
    pass

# Configure SQLite database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///id_users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# Define database model for storing ID details
class IdDetails(db.Model):
    """Database table schema for ID details"""
    id: Mapped[str] = mapped_column(String, primary_key=True)  # Primary key
    first_name: Mapped[str] = mapped_column(String, nullable=False)
    last_name: Mapped[str] = mapped_column(String, nullable=False)
    date_of_birth: Mapped[str] = mapped_column(String, nullable=False)
    age: Mapped[int] = mapped_column(Integer, nullable=False)
    sex: Mapped[str] = mapped_column(String)
    nationality: Mapped[str] = mapped_column(String)
    id_type: Mapped[str] = mapped_column(String)
    status: Mapped[str] = mapped_column(String)
    warning: Mapped[list] = mapped_column(String)  # Stored as JSON string
    doc_img: Mapped[str] = mapped_column(String, nullable=False)  # Document image
    face_img: Mapped[str] = mapped_column(String, nullable=False)  # Face image

# Create database tables if they don't exist
with app.app_context():
    db.create_all()

# API configuration
API_KEY = os.environ.get("API_KEY")
api_url = os.environ.get("API_URL")

# Build the API request payload
payload = {
    "profile": verify.profile_id,       # Profile ID from Verify instance
    "document": verify.document_base64,  # Base64 encoded document image
    "face": verify.face_base64           # Base64 encoded face image
}

# Set up API request headers
headers = {
    'X-API-KEY': API_KEY,
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

# Send POST request to the API
response = requests.post(api_url, headers=headers, data=json.dumps(payload))
r = response.json()  # Parse JSON response

# Prepare and store the parsed data in the database
new_id_details = IdDetails(
    id=r["data"]["documentNumber"][0]["value"],
    first_name=r["data"]["firstName"][0]["value"],
    last_name=r["data"]["lastName"][0]["value"],
    date_of_birth=r["data"]["dob"][0]["value"],
    age=r["data"]["age"][0]["value"],
    sex=r["data"]["sex"][0]["value"],
    nationality=r["data"]["nationalityFull"][0]["value"],
    id_type=r["data"]["documentName"][0]["value"],
    status=r["decision"],
    warning=json.dumps(r["warning"]),  # Convert warnings to JSON string
    doc_img=r["outputImage"]["front"],  # Extract front document image
    face_img=r["outputImage"]["face"]   # Extract face image
)

# Add the new record to the database and commit changes
with app.app_context():
    db.session.add(new_id_details)
    db.session.commit()

# Print the API response
print(response.text)

# Uncomment to run the app
# if __name__ == "__main__":
#     app.run(debug=True)


