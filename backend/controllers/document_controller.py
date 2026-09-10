import os
from pathlib import Path

from sqlalchemy.orm import Session

from models.document import Document


# --------------------------------------------------
# CONFIGURATION
# --------------------------------------------------

UPLOAD_FOLDER = Path("uploads/documents")

ALLOWED_EXTENSIONS = {"pdf"}


# --------------------------------------------------
# HELPER
# --------------------------------------------------

def allowed_file(filename):
    """Check whether the uploaded file is a PDF."""

    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower()
        in ALLOWED_EXTENSIONS
    )


# --------------------------------------------------
# UPLOAD DOCUMENT
# --------------------------------------------------

def upload_document(file, equipment_id, user_id, db: Session):
    """
    Save a maintenance PDF and create its database record.

    This version uses standard SQLAlchemy instead of
    Flask-SQLAlchemy.
    """

    if not file:
        return {
            "message": "No file provided"
        }, 400

    if not file.filename:
        return {
            "message": "No file selected"
        }, 400

    # Only PDF files
    if not allowed_file(file.filename):
        return {
            "message": "Only PDF files are allowed"
        }, 400

    # Create upload directory
    UPLOAD_FOLDER.mkdir(
        parents=True,
        exist_ok=True
    )

    # Get filename
    filename = Path(file.filename).name

    # Basic filename sanitization
    filename = filename.replace(" ", "_")

    file_path = UPLOAD_FOLDER / filename

    # Avoid overwriting existing file
    if file_path.exists():
        return {
            "message": "A file with this name already exists"
        }, 409

    # Save physical file
    file.save(str(file_path))

    # Convert equipment_id if provided
    if equipment_id is not None:
        try:
            equipment_id =