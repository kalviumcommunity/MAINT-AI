from sqlalchemy.orm import Session

from models.query import Query


# --------------------------------------------------
# GET QUERY HISTORY
# --------------------------------------------------

def get_history(user_id, db: Session):
    """
    Get troubleshooting query history for a user.
    """

    # Validate user_id
    if user_id is None:
        return {
            "message": "user_id is required"
        }, 400

    try:
        user_id = int(user_id)

    except (ValueError, TypeError):
        return {
            "message": "user_id must be an integer"
        }, 400

    # Get queries
    queries = (
        db.query(Query)
        .filter(Query.user_id == user_id)
        .order_by(Query.created_at.desc())
        .all()
    )

    history = []

    for query in queries:
        history.append({
            "query_id": query.query_id,
            "equipment_id": query.equipment_id,
            "issue_id": query.issue_id,
            "query_text": query.query_text,
            "ai_response": query.ai_response,
            "created_at": (
                query.created_at.isoformat()
                if query.created_at
                else None
            )
        })

    return {
        "message": "Query history retrieved successfully",
        "count": len(history),
        "history": history
    }, 200