# React Task Manager — Modul Praktikum

Project latihan React mandiri di folder `modul`. Aplikasi ini memakai tema pink lembut dari project tugas sebelumnya dan mempraktikkan komponen, props, state, hooks, Context API, penyimpanan lokal, dan routing.

## Menjalankan aplikasi

Persyaratan: Node.js dan npm.

```bash
node --version
npm --version
npm install
npm run dev
```

Buka URL lokal yang ditampilkan Vite, biasanya `http://localhost:5173`. Build dan tes otomatis:

```bash
npm run build
npm test
```

## Hasil eksekusi yang diharapkan

- Halaman **Beranda** menampilkan judul Task Manager, badge **Mode Layar Desktop** atau **Mode Layar Mobile**, kartu statistik tugas, form input, dan daftar tugas.
- Ketik judul tugas lalu pilih **Tambah** atau tekan Enter. Tugas langsung muncul dan tersimpan dengan key `tasks_data` di localStorage.
- Centang checkbox untuk menandai tugas selesai; hitungan statistik ikut berubah. Tombol **Hapus** menghapus satu tugas.
- Tombol **Hapus semua tugas** meminta konfirmasi terlebih dahulu.
- Buka **Tentang** untuk melihat penjelasan fitur dan jumlah tugas yang dibagikan melalui Context API.
- Halaman yang tidak dikenal memperlihatkan halaman **404**.
- Buka bagian **Latihan interaktif** di beranda untuk mencoba counter `useState` dan penambahan/penghapusan array immutable.

## Materi dan implementasi

1. **Setup dan HMR** — Vite menghidupkan development server; perubahan file langsung terlihat di browser. Simpan CSS header yang `background`-nya sudah pink untuk menguji HMR.
2. **Components & Props** — `Header` menerima props `title` dan `description`; `TaskItem` menerima data dan callbacks; `TaskForm` mengirim tugas baru ke parent; semua komponen UI memakai PropTypes.
3. **Children Props** — `Card` menerima `children` dan membungkus `TaskForm` di halaman beranda.
4. **State & Hooks** — counter dan array state bersifat interaktif; penghapusan menggunakan `filter` dan penambahan memakai salinan array. `useWindowSize` menunjukkan status mobile/desktop.
5. **Custom Hooks & localStorage** — `useLocalStorage` memulihkan dan menyimpan tugas, serta menyampaikan kegagalan penyimpanan.
6. **Context API & Routing** — `TaskProvider` berbagi operasi dan statistik; React Router menyediakan beranda, About, dan fallback 404.
7. **Latihan mandiri** — tombol hapus semua memakai `window.confirm`; halaman About menampilkan total tugas dari `useTasks()`.

## Struktur folder

```text
modul/
├── index.html
├── package.json
├── vite.config.js
└── src/
    ├── App.jsx
    ├── App.css
    ├── main.jsx
    ├── components/
    │   ├── Card/Card.jsx
    │   ├── Header/Header.jsx
    │   ├── Navbar/Navbar.jsx
    │   ├── TaskForm/TaskForm.jsx
    │   └── TaskItem/TaskItem.jsx
    ├── context/TaskContext.jsx
    ├── hooks/
    │   ├── useLocalStorage.js
    │   ├── useTasks.js
    │   └── useWindowSize.js
    ├── pages/
    │   ├── About/About.jsx
    │   ├── Home/Home.jsx
    │   └── NotFound/NotFound.jsx
    └── test/
        ├── App.test.jsx
        └── setup.js
```

## Laporan testing

Jalankan `npm test`. Tes React Testing Library mencakup tampilan awal, validasi input, tambah/simpan tugas, toggle statistik, hapus tugas, konfirmasi hapus semua, Context di About, 404, dan latihan counter/array.

Hasil verifikasi project:

| Pemeriksaan | Hasil |
| --- | --- |
| Vitest + React Testing Library | 9 tes lulus |
| Production build | Berhasil |
| Alur tambah tugas, navigasi About, dan badge mobile di browser | Berhasil |
