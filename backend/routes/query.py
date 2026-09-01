from flask import Blueprint, request, jsonify

query_router = Blueprint("query_router", __name__, url_prefix="/api/queries")


@query_router.route("/", methods=["POST"])
def create_query():
    data = request.get_json()

    return jsonify({
        "message": "Query received successfully",
        "query": data
    })