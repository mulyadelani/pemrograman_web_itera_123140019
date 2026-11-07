"""
Berkas     : main_password.py
Deskripsi  : Skrip Pengujian Modul password_gen
Praktikum  : Pemrograman Aplikasi Web (PAW) ITERA
Mahasiswa  : Mulya Delani (123140019)
"""

import sys
from pathlib import Path

# Pastikan folder modul berada dalam sys.path
DIREKTORI_KINI = Path(__file__).resolve().parent
if str(DIREKTORI_KINI) not in sys.path:
    sys.path.insert(0, str(DIREKTORI_KINI))

import password_gen as pg


def main() -> None:
    print("=" * 60)
    print("      PROGRAM PENGUJIAN GENERATOR PASSWORD ACAK")
    print("         Pengembang: Mulya Delani (123140019)")
    print("=" * 60)

    # 1. Menguji variasi panjang password
    daftar_panjang = [8, 10, 12, 16, 20]
    print("\n--- HASIL GENERASI PASSWORD BERBAGAI PANJANG ---")
    for panjang in daftar_panjang:
        pwd = pg.buat_password_acak(panjang=panjang, sertakan_simbol=True)
        print(f"Panjang {panjang:>2} karakter : {pwd}")

    # 2. Menguji mode alfanumerik murni (tanpa simbol)
    print("\n--- PASSWORD ALFANUMERIK (TANPA SIMBOL) ---")
    for i in range(1, 4):
        pwd_alpha = pg.buat_password_acak(panjang=10, sertakan_simbol=False)
        print(f"Sampel {i} (10 karakter): {pwd_alpha}")

    print("\n" + "=" * 60)
    print("Pengujian modul password_gen selesai dengan sukses!")
    print("=" * 60)


if __name__ == "__main__":
    main()

