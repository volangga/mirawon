from flask import Blueprint, jsonify
from utils.auth import require_api_key, rate_limiter

status_bp = Blueprint('status', __name__)

@status_bp.route('/status', methods=['GET'])
@require_api_key
@rate_limiter
def status():
    return jsonify({"success": True, "data": {"status": "ok", "message": "NuHa-AI is running and ready!"}, "error": None})
