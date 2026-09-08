from flask import Blueprint, request, jsonify

from models.query import Query

history_router = Blueprint(
    "history_router",
    __name__,
    url_prefix="/api/history"
)


@history_router.route("/", methods=["GET"])
def get_history():
    user_id = request.args.get("user_id")

    if not user_id:
        return jsonify({
            "message": "user_id is required"
        }), 400

    try:
        user_id = int(user_id)
    except (ValueError, TypeError):
        return jsonify({
            "message": "user_id must be an integer"
        }), 400

    queries = (
        Query.query
        .filter_by(user_id=user_id)
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
            "created_at": query.created_at.isoformat()
            if query.created_at else None
        })

    return jsonify({
        "message": "Query history retrieved successfully",
        "count": len(history),
        "history": history
    }), 200