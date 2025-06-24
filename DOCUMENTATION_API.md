# NuHa-AI API Documentation

## Endpoints

### 1. Generate Soal
- **URL:** `/generate-soal`
- **Method:** POST
- **Request JSON:**
  ```json
  {
    "topik": "Tema/topik soal",
    "jumlah": 5,
    "tingkat": "mudah|sedang|sulit"
  }
  ```
- **Response JSON:**
  ```json
  {
    "soal": "...hasil generate soal..."
  }
  ```

### 2. Training Model (Dummy)
- **URL:** `/train`
- **Method:** POST
- **Request JSON:**
  ```json
  {
    "dataset": [...],
    "params": {...}
  }
  ```
- **Response JSON:**
  ```json
  {
    "status": "success",
    "message": "Training dimulai (dummy endpoint, silakan implementasi sesuai kebutuhan)."
  }
  ```

## Catatan
- Semua endpoint menerima dan mengembalikan data dalam format JSON.
- Endpoint `/train` hanya dummy, silakan implementasi training model lokal/custom sesuai kebutuhan.
- API key Groq dikelola di `.env` dan hanya digunakan di backend.
