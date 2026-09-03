from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_documents(pages, chunk_size=1000, chunk_overlap=200):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )

    chunks = []

    for page in pages:
        page_chunks = splitter.split_text(page["text"])

        for chunk_index, chunk_text in enumerate(page_chunks):
            chunks.append({
                "chunk_index": chunk_index,
                "chunk_text": chunk_text,
                "page_number": page["page_number"]
            })

    return chunks