import base64
from image import doc



doc()
def encode_image(image_path):
    """Encodes an image file into base64."""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

class Verify():
    def __init__(self):
        self.document_image_path = "doc.jpg"
        self.face_image_path = "face.jpg"
        self.document_base64 = encode_image(self.document_image_path)
        self.face_base64 = encode_image(self.face_image_path)
        self.profile_id = "f38f7d62eed0475bbe4a8e11bc6968e0"



