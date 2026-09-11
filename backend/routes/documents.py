from sqlalchemy.orm import Session

from controllers.document_controller import (
    upload_document,
    get_all_documents,
    get_document,
    delete_document
)


# --------------------------------------------------
# UPLOAD DOCUMENT
# --------------------------------------------------

def upload(
    file,
    equipment_id,
    user_id,
    db: Session
):
    """
    Upload a PDF document.
    """

    return upload_document(
        file=file,
        equipment_id=equipment_id,
        user_id=user_id,
        db=db
    )


# --------------------------------------------------
# GET ALL DOCUMENTS
# --------------------------------------------------

def get_documents(db: Session):
    """
    Get all uploaded documents.
    """

    return get_all_documents(db)


# --------------------------------------------------
# GET DOCUMENT BY ID
# --------------------------------------------------

def get_single_document(
    document_id,
    db: Session
):
    """
    Get a document by ID.
    """

    return get_document(
        document_id,
        db
    )


# --------------------------------------------------
# DELETE DOCUMENT
# --------------------------------------------------

def delete_single_document(
    document_id,
    db: Session
):
    """
    Delete a document.
    """

    return delete_document(
        document_id,
        db
    )