from sqlalchemy import text

from backend.utils.database import engine


def create_document(document_name, document_type, file_path, equipment_id=None, uploaded_by=None):
    query = text("""
        INSERT INTO documents
        (document_name, document_type, file_path, equipment_id, uploaded_by)
        VALUES (:document_name, :document_type, :file_path, :equipment_id, :uploaded_by)
        RETURNING document_id
    """)

    with engine.begin() as connection:
        result = connection.execute(
            query,
            {
                "document_name": document_name,
                "document_type": document_type,
                "file_path": file_path,
                "equipment_id": equipment_id,
                "uploaded_by": uploaded_by
            }
        )

        return result.scalar_one()


def store_chunk(document_id, chunk_index, chunk_text, page_number, embedding):
    query = text("""
        INSERT INTO document_chunks
        (document_id, chunk_index, chunk_text, page_number, embedding)
        VALUES (:document_id, :chunk_index, :chunk_text, :page_number, :embedding)
        RETURNING chunk_id
    """)

    with engine.begin() as connection:
        result = connection.execute(
            query,
            {
                "document_id": document_id,
                "chunk_index": chunk_index,
                "chunk_text": chunk_text,
                "page_number": page_number,
                "embedding": embedding.tolist()
            }
        )

        return result.scalar_one()