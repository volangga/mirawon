from flask import request, jsonify
from functools import wraps
import time
from config import API_KEY, RATE_LIMIT

# Simple in-memory rate limiter per IP
rate_limit_cache = {}

def require_api_key(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        key = request.headers.get('X-API-KEY')
        if not key or key != API_KEY:
            return jsonify({"success": False, "data": None, "error": "Unauthorized: API key missing or invalid."}), 401
        return f(*args, **kwargs)
    return decorated

def rate_limiter(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        ip = request.remote_addr
        now = int(time.time())
        window = now // 60
        key = f"{ip}:{window}"
        count = rate_limit_cache.get(key, 0)
        if count >= RATE_LIMIT:
            return jsonify({"success": False, "data": None, "error": "Rate limit exceeded. Please wait."}), 429
        rate_limit_cache[key] = count + 1
        return f(*args, **kwargs)
    return decorated
