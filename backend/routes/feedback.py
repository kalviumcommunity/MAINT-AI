from sqlalchemy.orm import Session

from controllers.feedback_controller import create_feedback


# --------------------------------------------------
# SUBMIT FEEDBACK
# --------------------------------------------------

def submit_feedback(data, db: Session):
    """
    Submit feedback for a troubleshooting query.
    """

    return create_feedback(
        data,
        db
    )