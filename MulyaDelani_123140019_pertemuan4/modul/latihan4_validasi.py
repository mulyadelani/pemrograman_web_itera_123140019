"""
Berkas     : latihan4_validasi.py
Deskripsi  : Latihan Mandiri 4 - Fungsi Validator Password
Praktikum  : Pemrograman Aplikasi Web (PAW) ITERA
Mahasiswa  : Mulya Delani (123140019)
"""


def validasi_password(password: str) -> bool:
    """Memvalidasi kekuatan password berdasarkan kriteria:

    1. Panjang minimal 8 karakter.
    2. Mengandung setidaknya satu digit angka (0-9).

    Parameter:
        password (str): String password yang akan diuji.

    Returns:
        bool: True jika memenuhi kedua kriteria, False jika tidak.
    """
    if len(password) < 8:
        return False

    mengandung_angka = any(char.isdigit() for char in password)
    return mengandung_angka


def detail_analisis_password(password: str) -> None:
    """Mencetak analisis detail kelayakan password."""
    panjang = len(password)
    ada_angka = any(char.isdigit() for char in password)
    status_valid = validasi_password(password)
    status_str = "VALID (Lolos Syarat)" if status_valid else "TIDAK VALID"

    print(f"Password     : '{password}'")
    print(f"  - Panjang Karakter : {panjang} (Syarat >= 8: {'Ya' if panjang >= 8 else 'Tidak'})")
    print(f"  - Mengandung Angka : {'Ya' if ada_angka else 'Tidak'}")
    print(f"  - Kesimpulan       : {status_str}\n")


if __name__ == "__main__":
    print("=" * 60)
    print("        UJI COBA FUNGSI VALIDATOR PASSWORD")
    print("=" * 60)

    daftar_uji = [
        "pass123",              # Tidak valid (panjang < 8)
        "hanyahurufaja",        # Tidak valid (tanpa angka)
        "itera2024",            # Valid (panjang 9, ada angka)
        "Rahasia#789",          # Valid (panjang 11, ada angka)
        "1234567",              # Tidak valid (panjang 7)
        "mulya_delani_2023",    # Valid (panjang 17, ada angka)
        "admin",                # Tidak valid
    ]

    for kata_sandi in daftar_uji:
        detail_analisis_password(kata_sandi)

    print("=" * 60)

