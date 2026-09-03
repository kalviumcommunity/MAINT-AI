from flask import jsonify

from models.feedback import Feedback
from utils.database import db


def create_feedback(data):
    """Create feedback for a troubleshooting query."""

    if not data:
        return jsonify({
            "message": "Request body is required"
        }), 400

    query_id = data.get("query_id")
    user_id = data.get("user_id")
    rating = data.get("rating")
    comments = data.get("comments")

    # Validate query_id
    if query_id is None:
        return jsonify({
            "message": "query_id is required"
        }), 400

    # Validate rating
    if rating is None:
        return jsonify({
            "message": "rating is required"
        }), 400

    try:
        query_id = int(query_id)
        rating = int(rating)

        if user_id is not None:
            user_id = int(user_id)

    except (ValueError, TypeError):
        return jsonify({
            "message": "query_id, user_id and rating must be integers"
        }), 400

    # Rating must be 1-5
    if rating < 1 or rating > 5:
        return jsonify({
            "message": "rating must be between 1 and 5"
        }), 400

    # Create feedback
    feedback = Feedback(
        query_id=query_id,
        user_id=user_id,
        rating=rating,
        comments=comments
    )

    try:
        db.session.add(feedback)
        db.session.commit()

        return jsonify({
            "message": "Feedback submitted successfully",
            "feedback": {
                "feedback_id": feedback.feedback_id,
                "query_id": feedback.query_id,
                "user_id": feedback.user_id,
                "rating": feedback.rating,
                "comments": feedback.comments,
                "created_at": feedback.created_at
            }
        }), 201

    except Exception as e:
        db.session.rollback()

        return jsonify({
            "message": "Failed to submit feedback",
            "error": str(e)
        }), 500