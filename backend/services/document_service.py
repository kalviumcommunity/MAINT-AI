from pathlib import Path

from sqlalchemy.orm import Session

from models.document import Document

from backend.rag.document_processor import extract_text_from_pdf
from backend.rag.text_splitter import split_documents
from backend.rag.embeddings import generate_embeddings
from backend.rag.vector_store import store_chunk


# --------------------------------------------------
# PROCESS DOCUMENT
# --------------------------------------------------

def process_document(document_id: int, db: Session):
    """
    Process an uploaded PDF.

    Flow:

        PDF
         ↓
        Text extraction
         ↓
        Text splitting
         ↓
        BGE-M3 embeddings
         ↓
        pgvector
         ↓
        document_chunks
    """

    # --------------------------------------------------
    # 1. FIND DOCUMENT
    # --------------------------------------------------

    document = (
        db.query(Document)
        .filter(Document.document_id == document_id)
        .first()
    )

    if not document:
        return {
            "success": False,
            "message": "Document not found"
        }

    # --------------------------------------------------
    # 2. VALIDATE FILE
    # --------------------------------------------------

    if not document.file_path:
        return {
            "success": False,
            "message": "Document file path is missing"
        }

    file_path = Path(document.file_path)

    if not file_path.exists():
        return {
            "success": False,
            "message": "Document file does not exist"
        }

    try:

        # --------------------------------------------------
        # 3. EXTRACT TEXT
        # --------------------------------------------------

        pages = extract_text_from_pdf(
            str(file_path)
        )

        if not pages:
            return {
                "success": False,
                "message": "No text could be extracted from PDF"
            }

        # --------------------------------------------------
        # 4. SPLIT TEXT INTO CHUNKS
        # --------------------------------------------------

        chunks = split_documents(pages)

        if not chunks:
            return {
                "success": False,
                "message": "No chunks generated from document"
            }

        # --------------------------------------------------
        # 5. GENERATE BGE-M3 EMBEDDINGS
        # --------------------------------------------------

        texts = [
            chunk["chunk_text"]
            for chunk in chunks
        ]

        embeddings = generate_embeddings(texts)

        # --------------------------------------------------
        # 6. STORE CHUNKS IN PGVECTOR
        # --------------------------------------------------

        stored_chunks = 0

        for index, (chunk, embedding) in enumerate(
            zip(chunks, embeddings)
        ):

            store_chunk(
                document_id=document.document_id,
                chunk_index=index,
                chunk_text=chunk["chunk_text"],
                page_number=chunk["page_number"],
                embedding=embedding
            )

            stored_chunks += 1

        # --------------------------------------------------
        # 7. COMMIT DOCUMENT SESSION
        # --------------------------------------------------

        db.commit()

        return {
            "success": True,
            "message": "Document processed successfully",
            "document_id": document.document_id,
            "document_name": document.document_name,
            "pages": len(pages),
            "chunks": len(chunks),
           