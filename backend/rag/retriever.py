from sqlalchemy import text

from backend.utils.database import engine
from backend.rag.embeddings import generate_embeddings


def retrieve_chunks(query_text, k=3):
    query_embedding = generate_embeddings([query_text])[0].tolist()

    query = text("""
        SELECT
            chunk_id,
            document_id,
            chunk_text,
            page_number,
            embedding <=> CAST(:query_embedding AS vector) AS distance
        FROM document_chunks
        WHERE embedding IS NOT NULL
        ORDER BY embedding <=> CAST(:query_embedding AS vector)
        LIMIT :k
    """)

    with engine.connect() as connection:
        result = connection.execute(
            query,
            {
                "query_embedding": str(query_embedding),
                "k": k
            }
        )

        return result.fetchall()