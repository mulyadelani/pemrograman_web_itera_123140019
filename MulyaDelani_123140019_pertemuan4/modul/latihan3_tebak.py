# ===================================================
# Berkas: latihan3_tebak.py
# Deskripsi: Latihan Mandiri 3 - Game Tebak Angka Rahasia Sederhana
# Praktikum: Pemrograman Aplikasi Web (PAW) ITERA
# Mahasiswa: Mulya Delani (123140019)
# ===================================================

print("=" * 50)
print("     GAME TEBAK ANGKA RAHASIA (1 - 20)")
print("=" * 50)

angka_rahasia = 7
jumlah_percobaan = 0

while True:
    try:
        masukan = input("Masukkan tebakan angka Anda: ")
        tebakan = int(masukan)
        jumlah_percobaan += 1

        if tebakan < angka_rahasia:
            print("Terlalu kecil! Coba angka yang lebih besar.\n")
        elif tebakan > angka_rahasia:
            print("Terlalu besar! Coba angka yang lebih kecil.\n")
        else:
            print(f"Selamat, tebakan benar! Angka rahasianya adalah {angka_rahasia}.")
            print(f"Anda berhasil menebak dalam {jumlah_percobaan} kali percobaan.")
            break

    except ValueError:
        print("[Peringatan] Masukkan bilangan bulat yang valid!\n")
    except (KeyboardInterrupt, EOFError):
        print("\nPermainan dihentikan.")
        break

