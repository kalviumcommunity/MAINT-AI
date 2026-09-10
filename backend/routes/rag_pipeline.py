from backend.rag.rag_pipeline import build_rag_context


# --------------------------------------------------
# BUILD RAG CONTEXT
# --------------------------------------------------

def get_rag_context(query_text, k=3):
    """
    Retrieve relevant maintenance document chunks
    for a user query.
    """

    if not query_text:
        return {
            "success": False,
            "message": "query_text is required"
        }, 400

    try:
        result = build_rag_context(
            query_text=query_text,
            k=k
        )

        return {
            "success": True,
            "query": result["query"],
            "context": result["context"],
            "sources": result["sources"]
        }, 200

    except Exception:
        return {
            "success": False,
            "message": "Failed to retrieve RAG context"
        }, 500