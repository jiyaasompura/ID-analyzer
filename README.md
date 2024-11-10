
# ID Verification and Database Management System

A Flask-based application for verifying identity documents and facial images using an external API. The project stores extracted data in a SQLite database and provides an extendable framework for identity management tasks.

---

## Features

- **Flask Backend**: Simple and modular application structure.
- **SQLAlchemy ORM**: Object-relational mapping for managing data.
- **External API Integration**: Verifies documents and facial data via a third-party API.
- **Database Storage**: Extracted data is securely saved in a SQLite database.
- **Environment Configuration**: API keys and URLs managed via environment variables.

---

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Flask
- SQLAlchemy
- An active API key for the external identity verification service

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   - `API_KEY`: Your API key for the external service.
   - `API_URL`: The API endpoint for document verification.

4. Run the application:
   Uncomment the `if __name__ == "__main__"` block in the script and execute:
   ```bash
   python app.py
   ```

5. Verify the database:
   - The SQLite database `id_users.db` will be created in the project directory upon running the app.

---

## How It Works

1. **API Request**:
   - Sends a POST request containing:
     - Base64-encoded document and face images.
     - Profile ID.
   
2. **API Response Parsing**:
   - Extracts details such as name, date of birth, sex, nationality, ID type, and warnings.

3. **Database Storage**:
   - Saves user details, images, and verification status in `id_users.db`.

4. **Extendable Design**:
   - Ready for further integrations like front-end interfaces or additional APIs.

---

## Database Model

The database schema includes the following fields:

- `id`: Unique identifier (Primary Key)
- `first_name` and `last_name`: User's name
- `date_of_birth` and `age`: User's DOB and age
- `sex`: Gender
- `nationality`: Country of origin
- `id_type`: Document type (e.g., Passport)
- `status`: Verification status (e.g., Approved/Rejected)
- `warning`: JSON string of any warnings
- `doc_img` and `face_img`: URLs or encoded images

---

## API Configuration

Ensure your environment variables are set:

- `API_KEY`: API key for accessing the external service.
- `API_URL`: URL endpoint for document verification.

---

## Example API Response

The app expects the API response in the following format:

```json
{
  "data": {
    "documentNumber": [{"value": "123456"}],
    "firstName": [{"value": "John"}],
    "lastName": [{"value": "Doe"}],
    "dob": [{"value": "1990-01-01"}],
    "age": [{"value": 33}],
    "sex": [{"value": "Male"}],
    "nationalityFull": [{"value": "American"}],
    "documentName": [{"value": "Passport"}]
  },
  "decision": "Approved",
  "warning": ["Photo unclear"],
  "outputImage": {
    "front": "<base64_document_image>",
    "face": "<base64_face_image>"
  }
}
```

---

## Future Enhancements

- Add REST API routes for user interaction.
- Implement front-end integration for submissions and results.
- Support for other database backends like PostgreSQL or MySQL.
- Improved error handling and logging mechanisms.

---

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgments

- External API for identity verification services.
- Python and Flask communities for their extensive documentation.
