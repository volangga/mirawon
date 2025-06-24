from celery import Celery
import os
from ai.groq_client import chat_with_ai, generate_soal
from ai.prompt_builder import build_prompt
from config import GROQ_MODEL, GROQ_API_KEY

# Ganti ke Redis DB 2 agar benar-benar fresh
CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL", "redis://localhost:6379/2")
CELERY_RESULT_BACKEND = os.getenv("CELERY_RESULT_BACKEND", "redis://localhost:6379/2")

celery_app = Celery('nuha_ai', broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)

@celery_app.task
def async_chat_with_ai(messages, max_tokens=1024, temperature=0.7):
    return chat_with_ai(messages, max_tokens, temperature)

@celery_app.task
def async_generate_soal(topik, jumlah, tingkat, max_tokens=2048, temperature=0.7):
    prompt = build_prompt(topik, jumlah, tingkat)
    return generate_soal(prompt, max_tokens, temperature)
