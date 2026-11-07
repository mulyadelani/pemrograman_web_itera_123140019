# ===================================================
# Berkas: latihan2_suhu.py
# Deskripsi: Latihan Mandiri 2 - Kalkulator Konversi Suhu Interaktif
# Praktikum: Pemrograman Aplikasi Web (PAW) ITERA
# Mahasiswa: Mulya Delani (123140019)
# ===================================================

print("=" * 45)
print("     KALKULATOR KONVERSI TEMPERATUR SUHU")
print("=" * 45)

try:
    celsius = float(input("Masukkan temperatur dalam derajat Celcius (C): "))

    # Rumus konversi
    fahrenheit = (celsius * 9.0 / 5.0) + 32.0
    kelvin = celsius + 273.15

    print("\n--- HASIL KONVERSI SUHU ---")
    print(f"Temperatur Awal : {celsius:,.2f} °C")
    print(f"Fahrenheit      : {fahrenheit:,.2f} °F")
    print(f"Kelvin          : {kelvin:,.2f} K")
    print("=" * 45)

except ValueError:
    print("[Error] Masukan harus berupa angka numerik valid!")

