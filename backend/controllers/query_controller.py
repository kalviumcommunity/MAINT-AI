from flask import jsonify

from services.query_service import create_query


def handle_create_query(data):
    """Handle a new maintenance troubleshooting query."""

    if not data:
        return jsonify({
            "message": "Request body is required"
        }), 400

    query_text = data.get("query_text")

    # query_text is required
    if not query_text:
        return jsonify({
            "message": "query_text is required"
        }), 400

    # Validate IDs if provided
    user_id = data.get("user_id")
    equipment_id = data.get("equipment_id")
    issue_id = data.get("issue_id")

    try:
        if user_id is not None:
            data["user_id"] = int(user_id)

        if equipment_id is not None:
            data["equipment_id"] = int(equipment_id)

        if issue_id is not None:
            data["issue_id"] = int(issue_id)

    except (ValueError, TypeError):
        return jsonify({
            "message": "user_id, equipment_id and issue_id must be integers"
        }), 400

    try:
        result = create_query(data)

        return jsonify(result), 200

    except Exception as e:
        return jsonify({
            "message": "Failed to create query",
            "error": str(e)
        }), 500