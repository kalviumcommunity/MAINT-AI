from backend.rag.rag_pipeline import build_rag_context
from backend.services.llm_service import generate_troubleshooting_answer


def create_query(query_data):

    query_text = query_data["query_text"]

    # 1. Retrieve relevant documents using existing RAG pipeline
    rag_result = build_rag_context(query_text, k=3)

    # 2. Send retrieved context to Gemini
    answer = generate_troubleshooting_answer(
        query=query_text,
        context=rag_result["context"]
    )

    # 3. Return answer + sources
    return {
        "message": "Query processed successfully",

        "query": query_text,

        "answer": answer,

        "sources": rag_result["sources"]
    }