from pathlib import Path

from backend.rag.document_processor import extract_text_from_pdf
from backend.rag.text_splitter import split_documents
from backend.rag.embeddings import generate_embeddings
from backend.rag.vector_store import store_chunk


DATA_DIR = Path("data")

DOCUMENTS = {
    "industrial_motor_manual.pdf": 1,
    "centrifugal_pump_guide.pdf": 2,
    "air_compressor_guide.pdf": 3,
}


for filename, document_id in DOCUMENTS.items():
    file_path = DATA_DIR / filename

    print(f"\nProcessing: {filename}")

    pages = extract_text_from_pdf(str(file_path))
    chunks = split_documents(pages)

    texts = [chunk["chunk_text"] for chunk in chunks]
    embeddings = generate_embeddings(texts)

    for index, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
        store_chunk(
            document_id=document_id,
            chunk_index=index,
            chunk_text=chunk["chunk_text"],
            page_number=chunk["page_number"],
            embedding=embedding
        )

    print(f"Pages: {len(pages)}")
    print(f"Chunks: {len(chunks)}")
    print(f"Embeddings stored: {len(embeddings)}")

print("\nDocument ingestion completed successfully!")