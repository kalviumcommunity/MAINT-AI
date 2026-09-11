from sqlalchemy.orm import Session

from controllers.query_controller import handle_create_query


# --------------------------------------------------
# CREATE QUERY
# --------------------------------------------------

def create_query(data, db: Session):
    """
    Create and process a maintenance troubleshooting query.
    """

    return handle_create_query(
        data,
        db
    )