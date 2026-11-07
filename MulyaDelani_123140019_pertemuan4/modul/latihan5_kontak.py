"""
Berkas     : latihan5_kontak.py
Deskripsi  : Latihan Mandiri 5 - Katalog Kontak Sederhana (Dictionary)
Praktikum  : Pemrograman Aplikasi Web (PAW) ITERA
Mahasiswa  : Mulya Delani (123140019)
"""


def tampilkan_semua_kontak(buku_kontak: dict) -> None:
    """Menampilkan seluruh kontak yang tersimpan."""
    print("\n" + "=" * 45)
    print("           DAFTAR SELURUH KONTAK")
    print("=" * 45)
    if not buku_kontak:
        print("  (Buku kontak masih kosong)")
    else:
        for i, (nama, telepon) in enumerate(buku_kontak.items(), start=1):
            print(f"  {i}. {nama:<20} : {telepon}")
    print("=" * 45 + "\n")


def tambah_kontak(buku_kontak: dict, nama: str, nomor: str) -> None:
    """Menambahkan kontak baru atau memperbarui kontak yang sudah ada."""
    nama_bersih = nama.strip().title()
    nomor_bersih = nomor.strip()
    if not nama_bersih or not nomor_bersih:
        print("[Error] Nama dan nomor telepon tidak boleh kosong!\n")
        return
    buku_kontak[nama_bersih] = nomor_bersih
    print(f"[Sukses] Kontak '{nama_bersih}' berhasil disimpan dengan nomor: {nomor_bersih}\n")


def cari_kontak(buku_kontak: dict, nama: str) -> None:
    """Mencari nomor telepon berdasarkan nama kontak menggunakan method .get()."""
    nama_cari = nama.strip().title()
    # Menggunakan method .get() dengan default value jika key tidak ditemukan
    nomor = buku_kontak.get(nama_cari, None)
    if nomor:
        print(f"[Ditemukan] Kontak '{nama_cari}' -> No. Telepon: {nomor}\n")
    else:
        print(f"[Tidak Ditemukan] Kontak dengan nama '{nama_cari}' tidak ada dalam buku telepon.\n")


def main() -> None:
    """Fungsi antarmuka interaktif CLI untuk pengelolaan buku kontak."""
    # Data awal kontak
    kontak = {
        "Mulya Delani": "081234567890",
        "Ahmad Fadhilah": "085298765432",
        "Budi Santoso": "081377889900",
        "Citra Lestari": "087811223344"
    }

    print("*" * 50)
    print("       APLIKASI BUKU TELEPON SEDERHANA")
    print("*" * 50)

    while True:
        print("MENU PILIHAN:")
        print("1. Tampilkan Seluruh Kontak")
        print("2. Tambah Kontak Baru")
        print("3. Cari Nomor Kontak")
        print("4. Keluar")

        try:
            pilihan = input("Pilih menu (1-4): ").strip()
            if pilihan == "1":
                tampilkan_semua_kontak(kontak)
            elif pilihan == "2":
                input_nama = input("Masukkan nama kontak baru : ")
                input_nomor = input("Masukkan nomor telepon     : ")
                tambah_kontak(kontak, input_nama, input_nomor)
            elif pilihan == "3":
                input_cari = input("Masukkan nama yang dicari  : ")
                cari_kontak(kontak, input_cari)
            elif pilihan == "4":
                print("\nTerima kasih telah menggunakan aplikasi buku telepon!")
                break
            else:
                print("[Peringatan] Pilihan tidak valid. Masukkan angka 1 sampai 4.\n")
        except (KeyboardInterrupt, EOFError):
            print("\nProgram dihentikan.")
            break


if __name__ == "__main__":
    main()

