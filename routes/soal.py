from flask import Blueprint, request, jsonify
from celery_worker import async_generate_soal
from ai.prompt_builder import build_prompt
from utils.auth import require_api_key, rate_limiter

soal_bp = Blueprint('soal', __name__)

@soal_bp.route('/generate-soal', methods=['POST'])
@require_api_key
@rate_limiter
def generate():
    data = request.json
    try:
        topik = data['topik']
        jumlah = int(data['jumlah'])
        tingkat = data['tingkat']
        task = async_generate_soal.delay(topik, jumlah, tingkat)
        return jsonify({"success": True, "data": {"task_id": task.id}, "error": None})
    except (KeyError, ValueError) as e:
        return jsonify({"success": False, "data": None, "error": str(e)}), 400
    except Exception as e:
        return jsonify({"success": False, "data": None, "error": "Terjadi kesalahan pada server."}), 500

@soal_bp.route('/generate-soal/result/<task_id>', methods=['GET'])
@require_api_key
@rate_limiter
def soal_result(task_id):
    from celery_worker import celery_app
    result = celery_app.AsyncResult(task_id)
    if result.state == 'PENDING':
        return jsonify({"success": True, "data": {"status": "pending"}, "error": None})
    elif result.state == 'SUCCESS':
        return jsonify({"success": True, "data": {"status": "success", "soal": result.result}, "error": None})
    elif result.state == 'FAILURE':
        return jsonify({"success": False, "data": None, "error": str(result.info)}), 500
    else:
        return jsonify({"success": True, "data": {"status": result.state}, "error": None})
