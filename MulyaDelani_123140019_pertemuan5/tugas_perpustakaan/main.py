"""Skrip untuk menguji sistem manajemen perpustakaan."""

from .library import Library
from .library_item import Book, Magazine


def main() -> None:
    """Menambahkan, mencari, meminjam, dan menampilkan item."""
    perpustakaan = Library("Perpustakaan ITERA")
    perpustakaan.tambah_item(Book("B001", "Belajar Python", "Andi Wijaya", 320))
    perpustakaan.tambah_item(Book("B002", "Dasar Basis Data", "Siti Rahma", 280))
    perpustakaan.tambah_item(Magazine("M001", "Teknologi Hari Ini", 12, "November 2026"))

    perpustakaan.daftar_item_tersedia()
    perpustakaan.cari_item("B001")
    perpustakaan.cari_item("teknologi")

    perpustakaan.pinjam_item("B001")
    perpustakaan.cari_item("B001")
    perpustakaan.daftar_item_tersedia()
    perpustakaan.kembalikan_item("B001")
    perpustakaan.daftar_item_tersedia()


if __name__ == "__main__":
    main()
