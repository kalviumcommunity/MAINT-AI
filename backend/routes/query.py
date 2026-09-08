from flask import Blueprint, request

from controllers.query_controller import handle_create_query


query_router = Blueprint(
    "query_router",
    __name__,
    url_prefix="/api/queries"
)


@query_router.route("/", methods=["POST"])
def create_query():
    data = request.get_json()

    return handle_create_query(data)