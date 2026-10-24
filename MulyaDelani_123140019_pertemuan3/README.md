# Pertemuan 3 — Aplikasi React

Repository praktikum: **`pemrograman_web_itera_123140019`**  
Folder tugas: **`MulyaDelani_123140019_pertemuan3`**

Folder pertemuan ini berisi dua project React yang berdiri sendiri:

1. Aplikasi utama **RakBuku**, untuk mencatat koleksi buku pribadi.
2. **React Task Manager** di `modul/`, untuk latihan komponen, props, state, hooks, Context API, dan routing.

## Persyaratan

- Node.js dan npm telah terpasang. Periksa lewat terminal VS Code:

  ```bash
  node --version
  npm --version
  ```

## Menjalankan aplikasi utama RakBuku

Buka folder `MulyaDelani_123140019_pertemuan3` di VS Code. Jalankan perintah berikut pada terminal terintegrasi:

```bash
npm install
npm run dev
```

Buka alamat lokal yang ditampilkan Vite, biasanya `http://localhost:5173`.

## Menjalankan project latihan di folder modul

Buka terminal baru dan pindah ke folder `modul` terlebih dahulu:

```bash
cd modul
npm install
npm run dev
```

Buka alamat lokal yang ditampilkan. Jika aplikasi utama sedang berjalan, Vite dapat memilih port berikutnya (misalnya `5174`).

Jalankan tes atau build project modul dari folder `modul`:

```bash
npm test
npm run build
```

## RakBuku

RakBuku mendukung tambah, edit, dan hapus buku; filter status; pencarian judul atau penulis; serta halaman statistik. Data disimpan di `localStorage` browser.

![Screenshot halaman perpustakaan RakBuku](./screenshot.png)

Unit test aplikasi utama:

```bash
npm test
```

![Screenshot hasil unit test aplikasi utama](./test-results.png)

## React Task Manager

Project latihan lengkap beserta struktur komponen, latihan interaktif, petunjuk fitur, dan tes otomatis dijelaskan di [`modul/README.md`](./modul/README.md).

## Isi folder

```text
MulyaDelani_123140019_pertemuan3/
├── src/                  # Source aplikasi RakBuku
├── modul/                # Project latihan React Task Manager mandiri
├── screenshot.png        # Screenshot aplikasi RakBuku
├── test-results.png      # Screenshot hasil tes RakBuku
├── package.json          # Perintah dan dependensi RakBuku
├── package-lock.json     # Versi dependensi RakBuku
├── vite.config.js        # Konfigurasi Vite
├── vitest.config.js      # Tes aplikasi utama (tidak mencakup modul)
└── .gitignore            # Mengabaikan node_modules, dist, dan coverage
```

`node_modules/`, hasil build `dist/`, dan laporan coverage tidak perlu dikumpulkan; semuanya sudah tercantum di `.gitignore`, termasuk untuk project di `modul/`. File `package-lock.json` tetap disertakan agar versi dependensi dapat dipasang ulang secara konsisten.
