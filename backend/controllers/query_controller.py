from sqlalchemy.orm import Session

from services.query_service import create_query
from backend.rag.rag_pipeline import build_rag_context


# --------------------------------------------------
# CREATE QUERY
# --------------------------------------------------

def handle_create_query(data, db: Session):
    """
    Handle a new maintenance troubleshooting query.

    Flow:
        User query
            ↓
        RAG retrieval
            ↓
        Relevant document chunks
            ↓
        Query service
            ↓
        Database
    """

    if not data:
        return {
            "message": "Request body is required"
        }, 400

    query_text = data.get("query_text")

    # query_text is required
    if not query_text:
        return {
            "message": "query_text is required"
        }, 400

    # Validate IDs if provided
    user_id = data.get("user_id")
    equipment_id = data.get("equipment_id")
    issue_id = data.get("issue_id")

    try:
        if user_id is not None:
            user_id = int(user_id)

        if equipment_id is not None:
            equipment_id = int(equipment_id)

        if issue_id is not None:
            issue_id = int(issue_id)

    except (ValueError, TypeError):
        return {
            "message": (
                "user_id, equipment_id and issue_id "
                "must be integers"
            )
        }, 400

    try:

        # --------------------------------------------------
        # RAG RETRIEVAL
        # --------------------------------------------------

        rag_result = build_rag_context(
            query_text=query_text,
            k=3
        )

        # --------------------------------------------------
        # PREPARE QUERY DATA
        # --------------------------------------------------

        query_data = {
            "query_text": query_text,
            "user_id": user_id,
            "equipment_id": equipment_id,
            "issue_id": issue_id,
            "ai_response": rag_result["context"]
        }

        # --------------------------------------------------
        # SAVE QUERY
        # --------------------------------------------------

        result = create_query(
            query_data,
            db
        )

        # --------------------------------------------------
        # RETURN RESULT
        # --------------------------------------------------

        return {
            "message": "Query processed successfully",
            "query": result,
            "sources": rag_result["sources"]
        }, 