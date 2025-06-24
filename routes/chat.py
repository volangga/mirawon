from flask import Blueprint, request, jsonify
from celery_worker import async_chat_with_ai
from utils.auth import require_api_key, rate_limiter

chat_bp = Blueprint('chat', __name__)

@chat_bp.route('/chat', methods=['POST'])
@require_api_key
@rate_limiter
def chat():
    data = request.json
    messages = data.get('messages', [])
    if not isinstance(messages, list) or not messages:
        return jsonify({"success": False, "data": None, "error": "messages harus berupa list dan tidak boleh kosong."}), 400
    try:
        task = async_chat_with_ai.delay(messages)
        return jsonify({"success": True, "data": {"task_id": task.id}, "error": None})
    except Exception as e:
        return jsonify({"success": False, "data": None, "error": str(e)}), 500

@chat_bp.route('/chat/result/<task_id>', methods=['GET'])
@require_api_key
@rate_limiter
def chat_result(task_id):
    from celery_worker import celery_app
    result = celery_app.AsyncResult(task_id)
    if result.state == 'PENDING':
        return jsonify({"success": True, "data": {"status": "pending"}, "error": None})
    elif result.state == 'SUCCESS':
        return jsonify({"success": True, "data": {"status": "success", "reply": result.result}, "error": None})
    elif result.state == 'FAILURE':
        return jsonify({"success": False, "data": None, "error": str(result.info)}), 500
    else:
        return jsonify({"success": True, "data": {"status": result.state}, "error": None})
