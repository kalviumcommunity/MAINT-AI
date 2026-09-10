from sqlalchemy.orm import Session

from models.query import Query

from backend.rag.rag_pipeline import build_rag_context
from backend.services.llm_service import generate_answer


def create_query(data, db: Session):
    """
    Process a maintenance troubleshooting query.

    Flow:

        Question
            ↓
        BGE-M3
            ↓
        pgvector
            ↓
        RAG context
            ↓
        OpenAI
            ↓
        AI answer
            ↓
        PostgreSQL
    """

    query_text = data.get("query_text")

    if not query_text:
        return {
            "success": False,
            "message": "query_text is required"
        }

    user_id = data.get("user_id")
    equipment_id = data.get("equipment_id")
    issue_id = data.get("issue_id")

    try:

        # -------------------------------
        # RAG
        # -------------------------------

        rag_result = build_rag_context(
            query_text=query_text,
            k=3
        )

        # -------------------------------
        # OpenAI
        # -------------------------------

        llm_result = generate_answer(
            query_text=query_text,
            context=rag_result["context"]
        )

        if not llm_result["success"]:
            return llm_result

        ai_response = llm_result["answer"]

        # -------------------------------
        # Save query
        # -------------------------------

        query_record = Query(
            user_id=user_id,
            equipment_id=equipment_id,
            issue_id=issue_id,
            query_text=query_text,
            ai_response=ai_response
        )

        db.add(query_record)
        db.commit()
        db.refresh(query_record)

        # -------------------------------
        # Return
        # -------------------------------

        return {
            "success": True,
            "query_id": query_record.query_id,
            "query": query_text,
            "answer": ai_response,
            "sources": rag_result["sources"]
        }

    except Exception:
        db.rollback()
        raise