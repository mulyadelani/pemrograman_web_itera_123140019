"""
Berkas     : math_operations.py
Deskripsi  : Modul Matematika Kustom (Operasi Geometri & Konversi Suhu)
Praktikum  : Pemrograman Aplikasi Web (PAW) - Pertemuan 4
Nama       : Mulya Delani
NIM        : 123140019
"""

# ==============================================================================
# KONSTANTA MATEMATIKA
# ==============================================================================
PI: float = 3.141592653589793


# ==============================================================================
# FUNGSI-FUNGSI GEOMETRI (LUAS & KELILING)
# ==============================================================================

def luas_persegi(sisi: float) -> float:
    """Menghitung luas bangun datar persegi.

    Rumus:
        Luas = sisi * sisi

    Parameter:
        sisi (float): Panjang sisi persegi (harus > 0).

    Returns:
        float: Luas persegi.

    Raises:
        ValueError: Jika panjang sisi bernilai <= 0.
    """
    if sisi <= 0:
        raise ValueError("Panjang sisi persegi harus lebih besar dari 0.")
    return sisi * sisi


def keliling_persegi(sisi: float) -> float:
    """Menghitung keliling bangun datar persegi.

    Rumus:
        Keliling = 4 * sisi

    Parameter:
        sisi (float): Panjang sisi persegi (harus > 0).

    Returns:
        float: Keliling persegi.

    Raises:
        ValueError: Jika panjang sisi bernilai <= 0.
    """
    if sisi <= 0:
        raise ValueError("Panjang sisi persegi harus lebih besar dari 0.")
    return 4 * sisi


def luas_persegi_panjang(panjang: float, lebar: float) -> float:
    """Menghitung luas bangun datar persegi panjang.

    Rumus:
        Luas = panjang * lebar

    Parameter:
        panjang (float): Panjang persegi panjang (harus > 0).
        lebar (float): Lebar persegi panjang (harus > 0).

    Returns:
        float: Luas persegi panjang.

    Raises:
        ValueError: Jika panjang atau lebar bernilai <= 0.
    """
    if panjang <= 0 or lebar <= 0:
        raise ValueError("Panjang dan lebar persegi panjang harus lebih besar dari 0.")
    return panjang * lebar


def keliling_persegi_panjang(panjang: float, lebar: float) -> float:
    """Menghitung keliling bangun datar persegi panjang.

    Rumus:
        Keliling = 2 * (panjang + lebar)

    Parameter:
        panjang (float): Panjang persegi panjang (harus > 0).
        lebar (float): Lebar persegi panjang (harus > 0).

    Returns:
        float: Keliling persegi panjang.

    Raises:
        ValueError: Jika panjang atau lebar bernilai <= 0.
    """
    if panjang <= 0 or lebar <= 0:
        raise ValueError("Panjang dan lebar persegi panjang harus lebih besar dari 0.")
    return 2 * (panjang + lebar)


def luas_lingkaran(jari_jari: float) -> float:
    """Menghitung luas bangun datar lingkaran.

    Rumus:
        Luas = PI * jari_jari * jari_jari

    Parameter:
        jari_jari (float): Jari-jari lingkaran (harus > 0).

    Returns:
        float: Luas lingkaran.

    Raises:
        ValueError: Jika jari-jari bernilai <= 0.
    """
    if jari_jari <= 0:
        raise ValueError("Jari-jari lingkaran harus lebih besar dari 0.")
    return PI * (jari_jari ** 2)


def keliling_lingkaran(jari_jari: float) -> float:
    """Menghitung keliling bangun datar lingkaran.

    Rumus:
        Keliling = 2 * PI * jari_jari

    Parameter:
        jari_jari (float): Jari-jari lingkaran (harus > 0).

    Returns:
        float: Keliling lingkaran.

    Raises:
        ValueError: Jika jari-jari bernilai <= 0.
    """
    if jari_jari <= 0:
        raise ValueError("Jari-jari lingkaran harus lebih besar dari 0.")
    return 2 * PI * jari_jari


# ==============================================================================
# FUNGSI-FUNGSI KONVERSI TEMPERATUR SUHU
# ==============================================================================

def celsius_ke_fahrenheit(celsius: float) -> float:
    """Mengonversi nilai temperatur dari skala Celsius ke Fahrenheit.

    Rumus:
        F = (Celsius * 9/5) + 32

    Parameter:
        celsius (float): Derajat temperatur dalam skala Celsius.

    Returns:
        float: Nilai temperatur dalam skala Fahrenheit.
    """
    return (celsius * 9.0 / 5.0) + 32.0


def celsius_ke_kelvin(celsius: float) -> float:
    """Mengonversi nilai temperatur dari skala Celsius ke Kelvin.

    Rumus:
        K = Celsius + 273.15

    Parameter:
        celsius (float): Derajat temperatur dalam skala Celsius (harus >= -273.15).

    Returns:
        float: Nilai temperatur dalam skala Kelvin.

    Raises:
        ValueError: Jika nilai Celsius di bawah titik nol mutlak (-273.15 C).
    """
    if celsius < -273.15:
        raise ValueError("Temperatur tidak boleh lebih rendah dari nol mutlak (-273.15 C).")
    return celsius + 273.15


# ==============================================================================
# SELF-TESTING IDIOM (DIJALANKAN HANYA SAAT BERKAS DIEKSEKUSI LANGSUNG)
# ==============================================================================
if __name__ == "__main__":
    print("=" * 60)
    print("   [SELF-TEST] MODUL MATEMATIKA (math_operations.py)")
    print("=" * 60)
    print(f"Konstanta PI                   : {PI}")
    print(f"Test Luas Persegi (s=5)        : {luas_persegi(5.0)}")
    print(f"Test Keliling Persegi (s=5)    : {keliling_persegi(5.0)}")
    print(f"Test Luas Persegi Pjg (10x4)   : {luas_persegi_panjang(10.0, 4.0)}")
    print(f"Test Keliling Persegi Pjg      : {keliling_persegi_panjang(10.0, 4.0)}")
    print(f"Test Luas Lingkaran (r=7)      : {luas_lingkaran(7.0):.4f}")
    print(f"Test Keliling Lingkaran (r=7)  : {keliling_lingkaran(7.0):.4f}")
    print(f"Test 100 C -> Fahrenheit      : {celsius_ke_fahrenheit(100.0)} F")
    print(f"Test 0 C -> Kelvin             : {celsius_ke_kelvin(0.0)} K")
    print("=" * 60)
    print("Semua uji internal modul BERHASIL!")

