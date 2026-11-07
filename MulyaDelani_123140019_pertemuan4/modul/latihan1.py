# ===================================================
# Berkas: latihan1.py
# Deskripsi: Latihan Mandiri 1 - Identitas Diri & Eksperimen Print
# Praktikum: Pemrograman Aplikasi Web (PAW) ITERA
# Mahasiswa: Mulya Delani (123140019)
# ===================================================

# 1. Deklarasi data profil diri
nama = "Mulya Delani"
nim = "123140019"
angkatan = "2023"
program_studi = "Teknik Informatika"
minat_penelitian = "Web Development & Sistem Cerdas"

# 2. Eksperimen penggunaan parameter sep=' | '
print("--- PROFIL MAHASISWA (DENGAN PARAMETER SEP) ---")
print(nama, nim, angkatan, program_studi, minat_penelitian, sep=" | ")

# 3. Cetakan kartu identitas berbingkai karakter pagar (#) menggunakan escape character
bingkai = "#" * 60
print("\n" + bingkai)
print("#\t\tKARTU TANDA MAHASISWA ITERA\t\t   #")
print(bingkai)
print(f"# Nama Lengkap\t\t: {nama:<30} #")
print(f"# NIM\t\t\t: {nim:<30} #")
print(f"# Angkatan\t\t: {angkatan:<30} #")
print(f"# Program Studi\t\t: {program_studi:<30} #")
print(f"# Minat Penelitian\t: {minat_penelitian:<30} #")
print(bingkai + "\n")

