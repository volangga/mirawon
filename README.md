# VolAI

Aplikasi Python untuk AI API dengan Celery, siap untuk deployment di Render.

## Cara Menjalankan Lokal

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Jalankan aplikasi:
   ```bash
   python app.py
   ```
3. Jalankan worker Celery (opsional, jika menggunakan task async):
   ```bash
   celery -A celery_worker.celery worker --loglevel=info
   ```

## Deployment di Render
- Pastikan file `render.yaml` sudah sesuai dengan kebutuhan service (web service, background worker, dsb).
- Pastikan environment variable yang dibutuhkan sudah diatur di dashboard Render.

## Struktur Folder
- `app.py` : Entrypoint aplikasi utama
- `celery_worker.py` : Worker Celery
- `requirements.txt` : Daftar dependencies
- `render.yaml` : Konfigurasi Render
- `ai/`, `routes/`, `utils/` : Kode sumber

---

Silakan sesuaikan dokumentasi ini sesuai kebutuhan proyek Anda.
