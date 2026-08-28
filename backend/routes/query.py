from flask import Blueprint, request, jsonify

query_bp = Blueprint("query", __name__)

@query_bp.route("/query", methods=["POST"])
def query():
    data = request.json

    return jsonify({
        "query": data.get("query"),
        "message": "Query received"
    })