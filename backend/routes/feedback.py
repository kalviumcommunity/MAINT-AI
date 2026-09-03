from flask import Blueprint, request

from controllers.feedback_controller import create_feedback


feedback_router = Blueprint(
    "feedback_router",
    __name__,
    url_prefix="/api/feedback"
)


@feedback_router.route("/", methods=["POST"])
def submit_feedback():
    data = request.get_json()

    return create_feedback(data)