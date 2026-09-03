from sqlalchemy import text

from backend.utils.database import engine


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