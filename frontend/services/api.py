import requests

BACKEND_URL = "http://localhost:8000"


def submit_query(equipment_id: str, category: str, query_text: str, priority: str) -> dict:
    """Calls the backend /query endpoint.

    Returns:
        {"success": True, "data": {...}} on success
        {"success": False, "error": str} on failure
    """
    try:
        response = requests.post(
            f"{BACKEND_URL}/query/",
            json={
                "equipment_id": equipment_id,
                "category": category,
                "query_text": query_text,
                "priority": priority,
            },
            timeout=45,
        )
        response.raise_for_status()
        return {"success": True, "data": response.json()}

    except requests.exceptions.ConnectionError:
        return {"success": False, "error": "Could not connect to the backend. Is it running on port 8000?"}
    except requests.exceptions.Timeout:
        return {"success": False, "error": "The request timed out. Please try again."}
    except requests.exceptions.RequestException as e:
        return {"success": False, "error": str(e)}