"""Membuktikan bahwa nilai dan fungsi di Python merupakan objek."""


angka = 42
pesan = "Praktikum Pemrograman Web ITERA"
daftar_nilai = [85, 90, 78]

print("Tipe angka        :", type(angka), "| Class:", angka.__class__)
print("Tipe pesan        :", type(pesan), "| Class:", pesan.__class__)
print("Tipe daftar_nilai :", type(daftar_nilai), "| Class:", daftar_nilai.__class__)
print("\nManipulasi string:")
print("Huruf besar :", pesan.upper())
print("Pecah kata  :", pesan.split())


def salam() -> str:
    """Mengembalikan salam untuk menunjukkan fungsi juga objek."""
    return "Halo dari fungsi!"


print("\nHasil fungsi:", salam())
print("Tipe fungsi :", type(salam))
print("Identitas id:", hex(id(salam)))
