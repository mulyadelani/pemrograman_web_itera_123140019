"""
Berkas     : tugas1_bmi.py
Deskripsi  : Program Penghitung Body Mass Index (BMI) Sederhana
Praktikum  : Pemrograman Aplikasi Web (PAW) - Pertemuan 4
Nama       : Mulya Delani
NIM        : 123140019
"""


def hitung_bmi(berat: float, tinggi: float) -> float:
    """Menghitung nilai Body Mass Index (BMI).

    Parameter:
        berat (float): Berat badan dalam satuan kilogram (kg).
        tinggi (float): Tinggi badan dalam satuan meter (m).

    Returns:
        float: Nilai kalkulasi BMI.

    Raises:
        ValueError: Jika berat atau tinggi bernilai <= 0.
    """
    if berat <= 0 or tinggi <= 0:
        raise ValueError("Berat dan tinggi badan harus lebih besar dari nol!")
    return berat / (tinggi ** 2)


def tentukan_kategori_bmi(bmi: float) -> str:
    """Menentukan kategori status berat badan berdasarkan nilai BMI.

    Kriteria:
        - BMI < 18.5           : Berat badan kurang
        - 18.5 <= BMI < 25.0   : Berat badan normal
        - 25.0 <= BMI < 30.0   : Berat badan berlebih
        - BMI >= 30.0          : Obesitas

    Parameter:
        bmi (float): Nilai indeks massa tubuh (BMI).

    Returns:
        str: Deskripsi kategori berat badan.
    """
    if bmi < 18.5:
        return "Berat badan kurang"
    elif bmi < 25.0:
        return "Berat badan normal"
    elif bmi < 30.0:
        return "Berat badan berlebih"
    else:
        return "Obesitas"


def cetak_kartu_hasil(berat: float, tinggi: float, bmi: float, kategori: str) -> None:
    """Mencetak kartu informasi hasil perhitungan BMI dengan format yang rapi."""
    garis = "=" * 48
    print("\n" + garis)
    print("      HASIL ANALISIS BODY MASS INDEX (BMI)")
    print(garis)
    print(f"  Berat Badan     : {berat:.2f} kg")
    print(f"  Tinggi Badan    : {tinggi:.2f} m")
    print(f"  Nilai BMI       : {bmi:.2f}")
    print(f"  Kategori Status : {kategori}")
    print(garis)

    # Saran kesehatan berdasarkan kategori
    if kategori == "Berat badan normal":
        saran = "Pertahankan pola makan bergizi dan olahraga teratur."
    elif kategori == "Berat badan kurang":
        saran = "Tingkatkan asupan kalori bernutrisi dan konsultasi gizi."
    elif kategori == "Berat badan berlebih":
        saran = "Tingkatkan aktivitas fisik dan perhatikan porsi kalori."
    else:
        saran = "Disarankan konsultasi dokter atau ahli gizi untuk diet sehat."
    print(f"  Rekomendasi     : {saran}")
    print(garis + "\n")


def jalankan_demo_pengujian() -> None:
    """Menjalankan pengujian otomatis untuk memverifikasi seluruh kategori BMI."""
    print("\n" + "#" * 60)
    print("  SIMULASI PENGUJIAN OTOMATIS SELURUH KATEGORI BMI")
    print("#" * 60)

    sampel_data = [
        ("Pasien 1 (Kurus)", 45.0, 1.65),      # BMI ~ 16.53 (< 18.5)
        ("Pasien 2 (Ideal)", 63.0, 1.70),      # BMI ~ 21.80 (18.5 - 24.9)
        ("Pasien 3 (Overweight)", 78.0, 1.68), # BMI ~ 27.64 (25.0 - 29.9)
        ("Pasien 4 (Obesitas)", 95.0, 1.65),   # BMI ~ 34.89 (>= 30.0)
    ]

    for label, berat, tinggi in sampel_data:
        nilai_bmi = hitung_bmi(berat, tinggi)
        status = tentukan_kategori_bmi(nilai_bmi)
        print(f"[{label}]")
        print(f"  Berat: {berat} kg | Tinggi: {tinggi} m -> BMI: {nilai_bmi:.2f} | Status: {status}")
    print("#" * 60 + "\n")


def main() -> None:
    """Fungsi utama untuk interaksi pengguna atau demonstrasi."""
    print("=" * 48)
    print("   PROGRAM PENGHITUNG BODY MASS INDEX (BMI)")
    print("     Praktikum Pemrograman Aplikasi Web")
    print("=" * 48)

    try:
        input_berat = input("Masukkan berat badan (kg) [contoh: 65.5]: ").strip()
        input_tinggi = input("Masukkan tinggi badan (m)  [contoh: 1.70]: ").strip()

        # Konversi nilai
        berat = float(input_berat)
        tinggi = float(input_tinggi)

        # Antisipasi jika pengguna memasukkan tinggi dalam satuan cm (misal: 170 alih-alih 1.70)
        if tinggi > 3.0:
            print(f"[Info] Nilai tinggi {tinggi} terdeteksi dalam cm. Dikonversi menjadi {tinggi / 100:.2f} m.")
            tinggi /= 100

        nilai_bmi = hitung_bmi(berat, tinggi)
        kategori = tentukan_kategori_bmi(nilai_bmi)
        cetak_kartu_hasil(berat, tinggi, nilai_bmi, kategori)

    except ValueError as e:
        print(f"\n[Error Input]: {e}")
        print("Silakan masukkan nilai angka yang valid.")
    except (KeyboardInterrupt, EOFError):
        print("\nInput dibatalkan oleh pengguna.")

    # Tampilkan simulasi verifikasi jika diinginkan
    pilihan_demo = input("Apakah ingin melihat simulasi seluruh kategori? (y/n): ").strip().lower()
    if pilihan_demo in ("y", "ya", "yes"):
        jalankan_demo_pengujian()


if __name__ == "__main__":
    main()

