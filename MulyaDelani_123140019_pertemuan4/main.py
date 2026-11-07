"""
Berkas     : main.py
Deskripsi  : Program Pengujian dan Demonstrasi Modul math_operations
Praktikum  : Pemrograman Aplikasi Web (PAW) - Pertemuan 4
Nama       : Mulya Delani
NIM        : 123140019
"""

import sys
from pathlib import Path

# Memastikan direktori modul masuk ke sys.path agar dapat dieksekusi dari mana saja
DIREKTORI_KINI = Path(__file__).resolve().parent
if str(DIREKTORI_KINI) not in sys.path:
    sys.path.insert(0, str(DIREKTORI_KINI))

# ==============================================================================
# PENERAPAN MULTI-TEKNIK IMPOR MODUL (MINIMAL 2 TEKNIK IMPOR BERBEDA)
# ==============================================================================

# Teknik Impor 1: Mengimpor seluruh modul dengan alias (aliasing)
import math_operations as mo

# Teknik Impor 2: Mengimpor konstanta dan fungsi spesifik langsung ke namespace
from math_operations import (
    PI,
    luas_lingkaran,
    keliling_lingkaran,
    celsius_ke_fahrenheit,
    celsius_ke_kelvin
)


def cetak_header(judul: str) -> None:
    """Mencetak header seksi dengan dekorasi garis ASCII."""
    panjang = 65
    print("\n" + "=" * panjang)
    print(f"  {judul.upper()}")
    print("=" * panjang)


def demo_geometri_persegi() -> None:
    """Menguji fungsi luas dan keliling persegi (menggunakan teknik import aliasing: mo)."""
    cetak_header("1. Geometri Bangun Datar Persegi")
    daftar_sisi = [4.0, 7.5, 12.0]
    print(f"| {'Sisi (s)':^12} | {'Luas (s x s)':^18} | {'Keliling (4 x s)':^20} |")
    print("|" + "-" * 14 + "|" + "-" * 20 + "|" + "-" * 22 + "|")
    for s in daftar_sisi:
        luas = mo.luas_persegi(s)
        keliling = mo.keliling_persegi(s)
        print(f"| {s:^12.2f} | {luas:^18.2f} | {keliling:^20.2f} |")


def demo_geometri_persegi_panjang() -> None:
    """Menguji fungsi luas dan keliling persegi panjang (menggunakan modul mo)."""
    cetak_header("2. Geometri Bangun Datar Persegi Panjang")
    daftar_dimensi = [(6.0, 3.0), (10.0, 5.5), (15.0, 8.0)]
    print(f"| {'Panjang (p)':^12} | {'Lebar (l)':^11} | {'Luas (p x l)':^16} | {'Keliling 2*(p+l)':^18} |")
    print("|" + "-" * 14 + "|" + "-" * 13 + "|" + "-" * 18 + "|" + "-" * 20 + "|")
    for p, l in daftar_dimensi:
        luas = mo.luas_persegi_panjang(p, l)
        keliling = mo.keliling_persegi_panjang(p, l)
        print(f"| {p:^12.2f} | {l:^11.2f} | {luas:^16.2f} | {keliling:^18.2f} |")


def demo_geometri_lingkaran() -> None:
    """Menguji fungsi luas dan keliling lingkaran serta konstanta PI.

    (Menggunakan teknik direct import: luas_lingkaran, keliling_lingkaran, PI).
    """
    cetak_header("3. Geometri Bangun Datar Lingkaran (Direct Import)")
    print(f"Nilai Konstanta PI yang digunakan: {PI:.8f}")
    daftar_r = [3.5, 7.0, 14.0]
    print(f"| {'Jari-jari (r)':^15} | {'Luas (PI x r^2)':^20} | {'Keliling (2 x PI x r)':^22} |")
    print("|" + "-" * 17 + "|" + "-" * 22 + "|" + "-" * 24 + "|")
    for r in daftar_r:
        luas = luas_lingkaran(r)
        keliling = keliling_lingkaran(r)
        print(f"| {r:^15.2f} | {luas:^20.4f} | {keliling:^22.4f} |")


def demo_konversi_suhu() -> None:
    """Menguji fungsi konversi temperatur suhu Celsius ke Fahrenheit dan Kelvin.

    (Menggunakan teknik direct import: celsius_ke_fahrenheit, celsius_ke_kelvin).
    """
    cetak_header("4. Konversi Temperatur Suhu (Direct Import)")
    titik_suhu = [-40.0, 0.0, 25.0, 37.0, 100.0]
    print(f"| {'Celsius (C)':^13} | {'Fahrenheit (F)':^17} | {'Kelvin (K)':^15} | {'Keterangan Suhu':<15} |")
    print("|" + "-" * 15 + "|" + "-" * 19 + "|" + "-" * 17 + "|" + "-" * 18 + "|")
    
    keterangan_list = [
        "Titik temu C & F",
        "Titik beku air",
        "Suhu ruang nyaman",
        "Suhu tubuh normal",
        "Titik didih air"
    ]

    for c, ket in zip(titik_suhu, keterangan_list):
        f = celsius_ke_fahrenheit(c)
        k = celsius_ke_kelvin(c)
        print(f"| {c:^13.2f} | {f:^17.2f} | {k:^15.2f} | {ket:<16} |")


def main() -> None:
    """Titik masuk utama aplikasi untuk mendemonstrasikan seluruh fitur math_operations."""
    print("*" * 65)
    print("    PROGRAM UTAMA DEMONSTRASI MODUL MATEMATIKA PYTHON")
    print("         Pengembang: Mulya Delani (NIM: 123140019)")
    print("*" * 65)

    # 1. Menjalankan pengujian persegi
    demo_geometri_persegi()

    # 2. Menjalankan pengujian persegi panjang
    demo_geometri_persegi_panjang()

    # 3. Menjalankan pengujian lingkaran
    demo_geometri_lingkaran()

    # 4. Menjalankan pengujian konversi temperatur
    demo_konversi_suhu()

    print("\n" + "*" * 65)
    print("  SELURUH FUNGSI MODUL MATH_OPERATIONS TELAH SUKSES DIUJI!")
    print("*" * 65 + "\n")


if __name__ == "__main__":
    main()
