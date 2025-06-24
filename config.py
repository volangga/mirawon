import os
from dotenv import load_dotenv
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = os.getenv("GROQ_MODEL", "llama3-8b-8192")
API_KEY = os.getenv("PYTHON_API_KEY", "changeme")
RATE_LIMIT = int(os.getenv("PYTHON_RATE_LIMIT", 30))  # max 30 req/menit per IP
SENTRY_DSN = os.getenv("SENTRY_DSN", None)
