# Praktikum Pemrograman Web ITERA - Pertemuan 6

**Nama:** Mulya Delani

**NIM:** 123140019

**Kelas praktikum:** RA

Folder ini berisi jawaban praktik Pyramid dan tugas RESTful API manajemen mata kuliah. API mahasiswa dipertahankan sebagai contoh CRUD dari materi, sedangkan API mata kuliah merupakan tugas utama.

## Isi proyek

- `pyramid_mahasiswa/models/`: model ORM `Mahasiswa` dan `Matakuliah` serta registrasi SQLAlchemy.
- `pyramid_mahasiswa/views/`: endpoint CRUD JSON mahasiswa dan mata kuliah.
- `pyramid_mahasiswa/routes.py`: sepuluh route CRUD yang membedakan method HTTP.
- `pyramid_mahasiswa/alembic/versions/`: dua revisi berurutan untuk tabel `mahasiswa` dan `matakuliah`.
- `pyramid_mahasiswa/scripts/initialize_db.py`: seeding dua mahasiswa dan tiga mata kuliah; aman dijalankan ulang.
- `tests/test_validation.py`: pengujian field wajib, normalisasi teks, dan validasi angka positif.
- `development.ini`, `production.ini`, `setup.py`: konfigurasi serta dependensi aplikasi.

## Instalasi dan menjalankan

Persyaratan: Python 3.10+, PostgreSQL, dan PowerShell atau terminal lain.

1. Masuk ke folder ini, buat virtual environment, dan aktifkan:

   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

2. Pasang proyek dan dependensi:

   ```powershell
   python -m pip install --upgrade pip setuptools
   python -m pip install -e ".[testing]"
   ```

3. Buat database dan user PostgreSQL. Jalankan pada `psql` sebagai administrator:

   ```sql
   CREATE DATABASE pyramid_mahasiswa;
   CREATE USER pyramid_user WITH ENCRYPTED PASSWORD 'pyramid_pass';
   GRANT ALL PRIVILEGES ON DATABASE pyramid_mahasiswa TO pyramid_user;
   \c pyramid_mahasiswa
   GRANT ALL ON SCHEMA public TO pyramid_user;
   ```

   Sesuaikan kedua nilai `sqlalchemy.url` di `development.ini` bila kredensial atau host PostgreSQL berbeda (satu untuk aplikasi, satu untuk Alembic). Atau, untuk tidak menyimpan password di file, set `DATABASE_URL` di PowerShell; nilai ini dipakai oleh aplikasi, Alembic, dan skrip seeding:

   ```powershell
   $env:DATABASE_URL = "postgresql+psycopg2://postgres:YOUR_PASSWORD@localhost:5432/pyramid_mahasiswa"
   ```

4. Terapkan migrasi dan masukkan data contoh:

   ```powershell
   alembic -c development.ini upgrade head
   python -m pyramid_mahasiswa.scripts.initialize_db development.ini
   ```

5. Jalankan API:

   ```powershell
   pserve development.ini --reload
   ```

   Server lokal tersedia di `http://localhost:6543`. Endpoint `/` mengembalikan informasi API.

## API mata kuliah

| Method | Endpoint | Fungsi |
|---|---|---|
| GET | `/api/matakuliah` | Daftar semua mata kuliah |
| GET | `/api/matakuliah/{id}` | Detail mata kuliah; 404 bila tidak ada |
| POST | `/api/matakuliah` | Tambah data; wajib `kode_mk`, `nama_mk`, `sks`, `semester` |
| PUT | `/api/matakuliah/{id}` | Perbarui satu atau lebih field |
| DELETE | `/api/matakuliah/{id}` | Hapus data; 404 bila tidak ada |

`sks` dan `semester` harus bilangan bulat positif (bukan boolean atau teks). Kode mata kuliah harus unik. Permintaan tidak valid menghasilkan 400; data yang tidak ditemukan menghasilkan 404.

Contoh pengujian PowerShell (server harus aktif pada terminal lain):

```powershell
curl.exe http://localhost:6543/api/matakuliah
curl.exe http://localhost:6543/api/matakuliah/1

# curl.exe di Windows PowerShell dapat menghapus tanda kutip JSON pada argumen.
# Kirim body melalui file agar payload tetap JSON yang valid.
$bodyPath = Join-Path $env:TEMP "matakuliah.json"
$body = @{ kode_mk = "IF9999"; nama_mk = "Pengujian API"; sks = 3; semester = 5 } |
  ConvertTo-Json -Compress
[System.IO.File]::WriteAllText($bodyPath, $body, [System.Text.Encoding]::ASCII)
$postResponse = curl.exe --silent --show-error --include `
  -X POST http://localhost:6543/api/matakuliah `
  -H "Content-Type: application/json" `
  --data-binary "@$bodyPath"
$postResponse
$created = $postResponse[-1] | ConvertFrom-Json
$id = $created.matakuliah.id

$body = @{ nama_mk = "Basis Data Lanjut"; sks = 4 } | ConvertTo-Json -Compress
[System.IO.File]::WriteAllText($bodyPath, $body, [System.Text.Encoding]::ASCII)
curl.exe -X PUT "http://localhost:6543/api/matakuliah/$id" `
  -H "Content-Type: application/json" `
  --data-binary "@$bodyPath"

curl.exe -X DELETE "http://localhost:6543/api/matakuliah/$id"
curl.exe -i "http://localhost:6543/api/matakuliah/$id"
Remove-Item $bodyPath
```

Uji validasi 400:

```powershell
$bodyPath = Join-Path $env:TEMP "matakuliah-invalid.json"
$body = @{ kode_mk = "IF9998"; nama_mk = "Tanpa SKS"; semester = 5 } |
  ConvertTo-Json -Compress
[System.IO.File]::WriteAllText($bodyPath, $body, [System.Text.Encoding]::ASCII)
curl.exe -i -X POST http://localhost:6543/api/matakuliah `
  -H "Content-Type: application/json" `
  --data-binary "@$bodyPath"

Remove-Item $bodyPath
```

Untuk menguji respons 404, minta ID yang tidak ada, misalnya `GET /api/matakuliah/999999`, lalu hapus data dengan DELETE dan minta ID itu lagi.

## Praktik dan checkpoint materi

| Tahap | Verifikasi / jawaban |
|---|---|
| 0. Perangkat inti | `python --version` memeriksa interpreter; `psql --version` memeriksa client PostgreSQL. Python yang dipakai untuk menyiapkan folder ini adalah 3.13.3. |
| 1. Virtual environment | Buat/aktifkan `venv`, lalu `python -m pip list`; paket Pyramid, Alembic, SQLAlchemy, dan Waitress harus terpasang setelah langkah instalasi. |
| 2. Struktur proyek | Lapisan `models`, `views`, konfigurasi `.ini`, skrip, dan migrasi tersedia pada struktur folder ini. |
| 3. Koneksi PostgreSQL | Uji dengan `psql -h localhost -U pyramid_user -d pyramid_mahasiswa`; berhasil bila prompt database terbuka. |
| 4. Model ORM | `Mahasiswa` dan `Matakuliah` terdaftar di `models/__init__.py`; metadata keduanya digunakan Alembic. |
| 5. Migrasi & seeding | Jalankan `alembic -c development.ini upgrade head`, lalu skrip `initialize_db`; data awal bisa diperiksa melalui `SELECT * FROM matakuliah;`. |
| 6. Views | Views mahasiswa dan mata kuliah menerapkan JSON, validasi input, status 400/404, serta operasi CRUD. |
| 7. URL dispatch | Setiap route pada `routes.py` memasang predicate `request_method` yang sesuai dengan view. |
| 8. Pengujian API | Jalankan kelima operasi CRUD dan skenario invalid/404 yang dicontohkan di atas. |

Tahap yang membutuhkan PostgreSQL/server belum dijalankan di lingkungan penyusunan ini. Tes unit validasi dapat dijalankan tanpa database:

```powershell
python -m pytest
```

## Bukti pengujian untuk pengumpulan

Berikut tangkapan layar hasil pengujian API menggunakan cURL:

### GET

![Bukti pengujian GET](screenshots/01_get.png)

### POST

![Bukti pengujian POST](screenshots/02_post.png)

### PUT

![Bukti pengujian PUT](screenshots/03_put.png)

### DELETE

![Bukti pengujian DELETE](screenshots/04_delete.png)

### Error 404

![Bukti pengujian error 404](screenshots/05_error_404.png)

### Error 400

![Bukti pengujian error 400](screenshots/06_error_400.png)

## Catatan konfigurasi produksi

`production.ini` memakai URL database contoh sebagai placeholder. Ganti nilainya dengan konfigurasi database deployment sebelum dipakai; jangan menyimpan password database produksi ke repositori.
