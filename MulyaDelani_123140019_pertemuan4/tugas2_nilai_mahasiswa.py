"""
Berkas     : tugas2_nilai_mahasiswa.py
Deskripsi  : Program Pengelolaan Data dan Penilaian Mahasiswa
Praktikum  : Pemrograman Aplikasi Web (PAW) - Pertemuan 4
Nama       : Mulya Delani
NIM        : 123140019
"""

from typing import List, Dict, Tuple, Any


def hitung_nilai_akhir(uts: float, uas: float, tugas: float) -> float:
    """Menghitung nilai akhir mahasiswa berdasarkan komposisi bobot:

    - UTS   : 30%
    - UAS   : 40%
    - Tugas : 30%

    Formula:
        Nilai Akhir = (0.30 * UTS) + (0.40 * UAS) + (0.30 * Tugas)

    Parameter:
        uts (float): Nilai Ujian Tengah Semester (0 - 100).
        uas (float): Nilai Ujian Akhir Semester (0 - 100).
        tugas (float): Nilai Tugas / Praktikum (0 - 100).

    Returns:
        float: Nilai akhir terbobot.
    """
    return (0.30 * uts) + (0.40 * uas) + (0.30 * tugas)


def tentukan_grade(nilai_akhir: float) -> str:
    """Menentukan grade huruf berdasarkan perolehan nilai akhir.

    Kriteria:
        - A : Nilai akhir >= 80
        - B : 70 <= Nilai akhir < 80
        - C : 60 <= Nilai akhir < 70
        - D : 50 <= Nilai akhir < 60
        - E : Nilai akhir < 50

    Parameter:
        nilai_akhir (float): Nilai akhir hasil pembobotan.

    Returns:
        str: Grade huruf (A, B, C, D, atau E).
    """
    if nilai_akhir >= 80.0:
        return "A"
    elif nilai_akhir >= 70.0:
        return "B"
    elif nilai_akhir >= 60.0:
        return "C"
    elif nilai_akhir >= 50.0:
        return "D"
    else:
        return "E"


def proses_data_mahasiswa(daftar_mahasiswa: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Memproses daftar data mahasiswa dengan menghitung nilai akhir dan menentukan grade.

    Parameter:
        daftar_mahasiswa (list): List of dictionary berisi data mentah mahasiswa.

    Returns:
        list: List of dictionary yang telah diperkaya dengan nilai_akhir dan grade.
    """
    hasil_proses = []
    for mhs in daftar_mahasiswa:
        # Buat salinan agar tidak memutasi dictionary asli secara tidak sengaja
        data = mhs.copy()
        akhir = hitung_nilai_akhir(data["nilai_uts"], data["nilai_uas"], data["nilai_tugas"])
        data["nilai_akhir"] = round(akhir, 2)
        data["grade"] = tentukan_grade(akhir)
        hasil_proses.append(data)
    return hasil_proses


def tampilkan_tabel_mahasiswa(daftar_mahasiswa: List[Dict[str, Any]]) -> None:
    """Menampilkan tabel data mahasiswa secara rapi ke konsol dengan format f-string.

    Parameter:
        daftar_mahasiswa (list): List of dictionary mahasiswa yang telah diproses.
    """
    garis_pembatas = "+" + "-" * 6 + "+" + "-" * 24 + "+" + "-" * 14 + "+" + "-" * 9 + "+" + "-" * 9 + "+" + "-" * 9 + "+" + "-" * 14 + "+" + "-" * 8 + "+"
    
    print("\n" + "=" * 90)
    print("                    TABEL REKAPITULASI HASIL NILAI MAHASISWA")
    print("                        Praktikum Pemrograman Aplikasi Web")
    print("=" * 90)
    print(garis_pembatas)
    print(f"| {'No':^4} | {'Nama Mahasiswa':<22} | {'NIM':^12} | {'UTS':^7} | {'UAS':^7} | {'Tugas':^7} | {'Nilai Akhir':^12} | {'Grade':^6} |")
    print(garis_pembatas)

    for i, mhs in enumerate(daftar_mahasiswa, start=1):
        nama = mhs["nama"]
        nim = mhs["nim"]
        uts = f"{mhs['nilai_uts']:.1f}"
        uas = f"{mhs['nilai_uas']:.1f}"
        tugas = f"{mhs['nilai_tugas']:.1f}"
        akhir = f"{mhs['nilai_akhir']:.2f}"
        grade = mhs["grade"]
        print(f"| {i:^4} | {nama:<22} | {nim:^12} | {uts:>7} | {uas:>7} | {tugas:>7} | {akhir:>12} | {grade:^6} |")

    print(garis_pembatas)


def cari_ekstrem_nilai(daftar_mahasiswa: List[Dict[str, Any]]) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    """Mencari data mahasiswa dengan nilai akhir tertinggi dan terendah.

    Parameter:
        daftar_mahasiswa (list): List of dictionary mahasiswa yang telah memiliki 'nilai_akhir'.

    Returns:
        tuple: (mahasiswa_tertinggi, mahasiswa_terendah)
    """
    if not daftar_mahasiswa:
        raise ValueError("Daftar mahasiswa kosong!")
    
    tertinggi = max(daftar_mahasiswa, key=lambda m: m["nilai_akhir"])
    terendah = min(daftar_mahasiswa, key=lambda m: m["nilai_akhir"])
    return tertinggi, terendah


def tampilkan_statistik_ekstrem(tertinggi: Dict[str, Any], terendah: Dict[str, Any]) -> None:
    """Mencetak kartu informasi mahasiswa peraih nilai tertinggi dan terendah."""
    print("\n" + "=" * 50)
    print("           RINGKASAN STATISTIK KELAS")
    print("=" * 50)
    print(">>> MAHASISWA DENGAN NILAI TERTINGGI <<<")
    print(f"  Nama        : {tertinggi['nama']}")
    print(f"  NIM         : {tertinggi['nim']}")
    print(f"  Nilai Akhir : {tertinggi['nilai_akhir']:.2f}")
    print(f"  Grade       : {tertinggi['grade']}")
    print("-" * 50)
    print(">>> MAHASISWA DENGAN NILAI TERENDAH <<<")
    print(f"  Nama        : {terendah['nama']}")
    print(f"  NIM         : {terendah['nim']}")
    print(f"  Nilai Akhir : {terendah['nilai_akhir']:.2f}")
    print(f"  Grade       : {terendah['grade']}")
    print("=" * 50 + "\n")


def main() -> None:
    """Fungsi utama untuk menjalankan program rekapitulasi nilai."""
    # List memuat 7 data mahasiswa (lebih dari syarat minimal 5)
    # Mencakup representasi spektrum nilai dan grade A sampai E
    data_mentah_mahasiswa = [
        {
            "nama": "Mulya Delani",
            "nim": "123140019",
            "nilai_uts": 92.0,
            "nilai_uas": 95.0,
            "nilai_tugas": 90.0
        },
        {
            "nama": "Ahmad Fadhilah",
            "nim": "123140001",
            "nilai_uts": 82.5,
            "nilai_uas": 85.0,
            "nilai_tugas": 88.0
        },
        {
            "nama": "Budi Santoso",
            "nim": "123140025",
            "nilai_uts": 75.0,
            "nilai_uas": 72.0,
            "nilai_tugas": 78.0
        },
        {
            "nama": "Citra Lestari",
            "nim": "123140040",
            "nilai_uts": 65.0,
            "nilai_uas": 68.0,
            "nilai_tugas": 62.0
        },
        {
            "nama": "Dedi Kurniawan",
            "nim": "123140055",
            "nilai_uts": 55.0,
            "nilai_uas": 52.0,
            "nilai_tugas": 58.0
        },
        {
            "nama": "Eka Saputra",
            "nim": "123140072",
            "nilai_uts": 40.0,
            "nilai_uas": 45.0,
            "nilai_tugas": 50.0
        },
        {
            "nama": "Farhan Alamsyah",
            "nim": "123140088",
            "nilai_uts": 88.0,
            "nilai_uas": 84.0,
            "nilai_tugas": 86.0
        }
    ]

    # Proses kalkulasi nilai dan grade
    data_terproses = proses_data_mahasiswa(data_mentah_mahasiswa)

    # Tampilkan tabel lengkap
    tampilkan_tabel_mahasiswa(data_terproses)

    # Temukan dan tampilkan mahasiswa ekstrem (tertinggi & terendah)
    mhs_tertinggi, mhs_terendah = cari_ekstrem_nilai(data_terproses)
    tampilkan_statistik_ekstrem(mhs_tertinggi, mhs_terendah)


if __name__ == "__main__":
    main()

