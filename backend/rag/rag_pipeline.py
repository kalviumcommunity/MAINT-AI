from backend.rag.retriever import retrieve_chunks


def build_rag_context(query_text, k=3):
    """
    Retrieve relevant maintenance document chunks for a user query
    and format them as RAG context with source information.
    """

    results = retrieve_chunks(query_text, k=k)

    context_parts = []
    sources = []

    for result in results:
        context_parts.append(
            f"[Source: Document {result.document_id}, "
            f"Page {result.page_number}]\n"
            f"{result.chunk_text}"
        )

        sources.append({
            "document_id": result.document_id,
            "page_number": result.page_number,
            "chunk_id": result.chunk_id,
            "distance": float(result.distance)
        })

    return {
        "query": query_text,
        "context": "\n\n".join(context_parts),
        "sources": sources
    }