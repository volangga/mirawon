import requests
from config import GROQ_API_KEY, GROQ_MODEL
from utils.logger import get_logger

logger = get_logger(__name__)

def generate_soal(prompt, max_tokens=2048, temperature=0.7):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": GROQ_MODEL,
        "messages": [
            {"role": "system", "content": "Anda adalah generator soal pilihan ganda."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": max_tokens,
        "temperature": temperature
    }
    try:
        response = requests.post("https://api.groq.com/openai/v1/chat/completions", json=payload, headers=headers)
        response.raise_for_status()
        result = response.json()
        return result.get("choices", [{}])[0].get("message", {}).get("content", "Gagal generate soal.")
    except Exception as e:
        logger.error(f"Gagal generate soal: {e}")
        return "Gagal generate soal."

def chat_with_ai(messages, max_tokens=1024, temperature=0.7):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": GROQ_MODEL,
        "messages": messages,
        "max_tokens": max_tokens,
        "temperature": temperature
    }
    try:
        response = requests.post("https://api.groq.com/openai/v1/chat/completions", json=payload, headers=headers)
        response.raise_for_status()
        result = response.json()
        return result.get("choices", [{}])[0].get("message", {}).get("content", "Maaf, AI tidak bisa menjawab saat ini.")
    except Exception as e:
        logger.error(f"Gagal chat dengan AI: {e}")
        return "Maaf, AI tidak bisa menjawab saat ini."
