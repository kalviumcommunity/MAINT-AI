from sqlalchemy.orm import Session

from models.feedback import Feedback


# --------------------------------------------------
# CREATE FEEDBACK
# --------------------------------------------------

def create_feedback(data, db: Session):
    """Create feedback for a troubleshooting query."""

    if not data:
        return {
            "message": "Request body is required"
        }, 400

    query_id = data.get("query_id")
    user_id = data.get("user_id")
    rating = data.get("rating")
    comments = data.get("comments")

    # Validate query_id
    if query_id is None:
        return {
            "message": "query_id is required"
        }, 400

    # Validate rating
    if rating is None:
        return {
            "message": "rating is required"
        }, 400

    # Convert values to integers
    try:
        query_id = int(query_id)
        rating = int(rating)

        if user_id is not None:
            user_id = int(user_id)

    except (ValueError, TypeError):
        return {
            "