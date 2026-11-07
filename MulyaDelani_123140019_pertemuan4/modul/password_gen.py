"""
Berkas     : password_gen.py
Deskripsi  : Modul Generator Password Acak
Praktikum  : Pemrograman Aplikasi Web (PAW) ITERA
Mahasiswa  : Mulya Delani (123140019)
"""

import random
import string


def buat_password_acak(panjang: int = 8, sertakan_simbol: bool = True) -> str:
    """Menghasilkan kata sandi acak yang aman dengan panjang tertentu.

    Parameter:
        panjang (int): Panjang karakter password (default 8, minimal 4).
        sertakan_simbol (bool): Menyertakan tanda baca/simbol khusus jika True.

    Returns:
        str: String kata sandi acak yang telah diacak susunannya.
    """
    if panjang < 4:
        raise ValueError("Panjang password minimal adalah 4 karakter demi keamanan!")

    # Mempersiapkan pool karakter dasar
    kumpulan_huruf = string.ascii_letters
    kumpulan_angka = string.digits
    kumpulan_simbol = "!@#$%^&*" if sertakan_simbol else ""

    pool_semua = kumpulan_huruf + kumpulan_angka + kumpulan_simbol

    # Menjamin setidaknya ada 1 huruf kecil, 1 huruf besar, dan 1 angka
    password_karakter = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(kumpulan_angka)
    ]

    if sertakan_simbol:
        password_karakter.append(random.choice(kumpulan_simbol))

    # Mengisi sisa panjang yang dibutuhkan secara acak dari seluruh pool
    sisa_panjang = panjang - len(password_karakter)
    for _ in range(sisa_panjang):
        password_karakter.append(random.choice(pool_semua))

    # Mengacak urutan agar posisinya tidak tertebak
    random.shuffle(password_karakter)

    return "".join(password_karakter)


if __name__ == "__main__":
    print("[TEST MODUL] Generator Password Acak:")
    print("Password 8 karakter  :", buat_password_acak(8))
    print("Password 12 karakter :", buat_password_acak(12))
    print("Password 16 karakter :", buat_password_acak(16, sertakan_simbol=True))

