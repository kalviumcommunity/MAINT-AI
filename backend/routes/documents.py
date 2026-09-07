from flask import Blueprint, request

from controllers.document_controller import (
    upload_document,
    get_all_documents,
    get_document,
    delete_document,
    update_processing_status
)

documents_router = Blueprint(
    "documents_router",
    __name__,
    url_prefix="/api/documents"
)


# Upload PDF
@documents_router.route("/", methods=["POST"])
def upload():
    file = request.files.get("file")
    data = request.form

    user_id = request.form.get("user_id")

    if user_id is not None:
        try:
            user_id = int(user_id)
        except ValueError:
            return {
                "message": "user_id must be an integer"
            }, 400

    return upload_document(file, data, user_id)


# Get all documents
@documents_router.route("/", methods=["GET"])
def get_documents():
    return get_all_documents()


# Get document by ID
@documents_router.route("/<int:document_id>", methods=["GET"])
def get_single_document(document_id):
    return get_document(document_id)


# Delete document
@documents_router.route("/<int:document_id>", methods=["DELETE"])
def delete_single_document(document_id):
    return delete_document(document_id)


# Update processing status
@documents_router.route("/<int:document_id>/status", methods=["PATCH"])
def update_status(document_id):
    data = request.get_json()

    if not data:
        return {
            "message": "Request body is required"
        }, 400

    status = data.get("status")
    chunk_count = data.get("chunk_count")

    return update_processing_status(
        document_id,
        status,
        chunk_count
    )