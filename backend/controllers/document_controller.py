import os
from werkzeug.utils import secure_filename
from flask import jsonify

from models.document import Document
from utils.database import db


# Upload directory
UPLOAD_FOLDER = "uploads/documents"

# Allowed file types
ALLOWED_EXTENSIONS = {"pdf"}


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

def upload_document(file, data, user_id):
    """
    Upload a maintenance PDF and create
    its database record.
    """

    if not file:
        return jsonify({
            "message": "No file provided"
        }), 400

    if file.filename == "":
        return jsonify({
            "message": "No file selected"
        }), 400

    # Only PDF files
    if not allowed_file(file.filename):
        return jsonify({
            "message": "Only PDF files are allowed"
        }), 400

    # Create upload directory
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    # Secure filename
    filename = secure_filename(file.filename)

    file_path = os.path.join(
        UPLOAD_FOLDER,
        filename
    )

    # Avoid overwriting an existing file
    if os.path.exists(file_path):
        return jsonify({
            "message": "A file with this name already exists"
        }), 409

    # Save file
    file.save(file_path)

    # Get file size
    file_size = os.path.getsize(file_path)

    # Optional fields
    description = data.get("description")
    category = data.get("category")

    equipment_id = data.get("equipment_id")

    # Convert equipment_id to integer if provided
    if equipment_id:
        try:
            equipment_id = int(equipment_id)
        except ValueError:
            return jsonify({
                "message": "equipment_id must be an integer"
            }), 400

    # Create document record
    document = Document(
        document_name=filename,
        document_type="PDF",
        description=description,
        file_path=file_path,
        file_size=file_size,
        category=category,
        equipment_id=equipment_id,
        processing_status="pending",
        chunk_count=0,
        uploaded_by=user_id
    )

    db.session.add(document)
    db.session.commit()

    return jsonify({
        "message": "Document uploaded successfully",
        "document": {
            "document_id": document.document_id,
            "document_name": document.document_name,
            "document_type": document.document_type,
            "description": document.description,
            "file_path": document.file_path,
            "file_size": document.file_size,
            "category": document.category,
            "equipment_id": document.equipment_id,
            "processing_status": document.processing_status,
            "chunk_count": document.chunk_count,
            "uploaded_by": document.uploaded_by,
            "uploaded_at": document.uploaded_at
        }
    }), 201


# --------------------------------------------------
# GET ALL DOCUMENTS
# --------------------------------------------------

def get_all_documents():
    """Return all maintenance documents."""

    documents = Document.query.order_by(
        Document.uploaded_at.desc()
    ).all()

    result = []

    for document in documents:
        result.append({
            "document_id": document.document_id,
            "document_name": document.document_name,
            "document_type": document.document_type,
            "description": document.description,
            "file_size": document.file_size,
            "category": document.category,
            "equipment_id": document.equipment_id,
            "processing_status": document.processing_status,
            "chunk_count": document.chunk_count,
            "uploaded_by": document.uploaded_by,
            "uploaded_at": document.uploaded_at,
            "updated_at": document.updated_at
        })

    return jsonify({
        "documents": result
    }), 200


# --------------------------------------------------
# GET DOCUMENT BY ID
# --------------------------------------------------

def get_document(document_id):
    """Return a specific document."""

    document = Document.query.get(document_id)

    if not document:
        return jsonify({
            "message": "Document not found"
        }), 404

    return jsonify({
        "document_id": document.document_id,
        "document_name": document.document_name,
        "document_type": document.document_type,
        "description": document.description,
        "file_path": document.file_path,
        "file_size": document.file_size,
        "category": document.category,
        "equipment_id": document.equipment_id,
        "processing_status": document.processing_status,
        "chunk_count": document.chunk_count,
        "uploaded_by": document.uploaded_by,
        "uploaded_at": document.uploaded_at,
        "updated_at": document.updated_at
    }), 200


# --------------------------------------------------
# DELETE DOCUMENT
# --------------------------------------------------

def delete_document(document_id):
    """Delete document from database and storage."""

    document = Document.query.get(document_id)

    if not document:
        return jsonify({
            "message": "Document not found"
        }), 404

    # Delete physical file
    if document.file_path:
        if os.path.exists(document.file_path):
            os.remove(document.file_path)

    # Delete database record
    db.session.delete(document)
    db.session.commit()

    return jsonify({
        "message": "Document deleted successfully"
    }), 200


# --------------------------------------------------
# UPDATE PROCESSING STATUS
# --------------------------------------------------

def update_processing_status(
    document_id,
    status,
    chunk_count=None
):
    """
    Update RAG document processing status.
    """

    document = Document.query.get(document_id)

    if not document:
        return jsonify({
            "message": "Document not found"
        }), 404

    allowed_statuses = {
        "pending",
        "processing",
        "completed",
        "failed"
    }

    if status not in allowed_statuses:
        return jsonify({
            "message": "Invalid processing status"
        }), 400

    document.processing_status = status

    if chunk_count is not None:
        document.chunk_count = chunk_count

    db.session.commit()

    return jsonify({
        "message": "Processing status updated",
        "document": {
            "document_id": document.document_id,
            "processing_status": document.processing_status,
            "chunk_count": document.chunk_count
        }
    }), 200