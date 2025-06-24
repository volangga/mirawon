# Cara Upload Folder VolAI ke GitHub

1. **Masuk ke folder VolAI**
   ```powershell
   cd c:\Aplikasi\VolAI
   ```
2. **Inisialisasi Git (jika belum)**
   ```powershell
   git init
   ```
3. **Tambahkan semua file**
   ```powershell
   git add .
   ```
4. **Commit perubahan**
   ```powershell
   git commit -m "Initial commit VolAI"
   ```
5. **Buat repository baru di GitHub**
   - Buka https://github.com dan klik "New Repository"
   - Isi nama repository, misal: `VolAI`, lalu klik "Create repository"
6. **Hubungkan ke repository GitHub**
   ```powershell
   git remote add origin https://github.com/USERNAME/VolAI.git
   ```
   (Ganti `USERNAME` dengan username GitHub Anda)
7. **Push ke GitHub**
   ```powershell
   git branch -M main
   git push -u origin main
   ```

---

**Catatan:**
- Jangan upload file `.env` atau file sensitif lain (sudah diatur di `.gitignore`).
- Setelah upload, Anda bisa langsung connect repository ini ke Render.
