from flask import Flask, request
from routes.soal import soal_bp
from routes.train import train_bp
from routes.chat import chat_bp
from routes.status import status_bp
from utils.logger import get_logger
from config import SENTRY_DSN

app = Flask(__name__)
app.register_blueprint(soal_bp)
app.register_blueprint(train_bp)
app.register_blueprint(chat_bp)
app.register_blueprint(status_bp)

logger = get_logger("NuHa-AI")

# Sentry integration (optional)
if SENTRY_DSN:
    import sentry_sdk
    sentry_sdk.init(dsn=SENTRY_DSN, traces_sample_rate=1.0)
    logger.info("Sentry enabled.")

@app.before_request
def log_request_info():
    logger.info(f"Request: {request.method} {request.path} | IP: {request.remote_addr} | Data: {request.get_json(silent=True)}")

@app.after_request
def log_response_info(response):
    logger.info(f"Response: {request.method} {request.path} | Status: {response.status_code}")
    return response

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

