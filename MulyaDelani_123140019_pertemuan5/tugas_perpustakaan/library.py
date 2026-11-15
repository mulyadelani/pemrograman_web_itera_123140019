"""Pengelolaan katalog dan pencarian item perpustakaan."""

from .library_item import LibraryItem


class Library:
    """Menyimpan koleksi secara privat dan menyediakan operasi katalog."""

    def __init__(self, nama: str) -> None:
        self.nama = nama
        self.__koleksi: dict[str, LibraryItem] = {}

    def tambah_item(self, item: LibraryItem) -> None:
        if item.item_id in self.__koleksi:
            raise ValueError(f"ID item {item.item_id!r} sudah terdaftar.")
        self.__koleksi[item.item_id] = item
        print(f"Item ditambahkan: {item.get_detail()}")

    def daftar_item_tersedia(self) -> list[LibraryItem]:
        """Mengembalikan dan mencetak item yang belum dipinjam."""
        tersedia = [item for item in self.__koleksi.values() if not item.is_dipinjam]
        print(f"\nKatalog tersedia di {self.nama}:")
        if not tersedia:
            print("Tidak ada item yang tersedia.")
        for item in tersedia:
            print(f"- [{item.item_id}] {item.get_detail()}")
        return tersedia

    def cari_item(self, kata_kunci: str) -> list[LibraryItem]:
        """Mencari berdasarkan ID persis atau judul tanpa membedakan kapital."""
        kunci = kata_kunci.strip().casefold()
        if not kunci:
            return []
        hasil = [
            item
            for item in self.__koleksi.values()
            if item.item_id.casefold() == kunci or kunci in item.judul.casefold()
        ]
        print(f"\nHasil pencarian {kata_kunci!r}:")
        if not hasil:
            print("Item tidak ditemukan.")
        for item in hasil:
            status = "Dipinjam" if item.is_dipinjam else "Tersedia"
            print(f"- [{item.item_id}] {item.get_detail()} | Status: {status}")
        return hasil

    def pinjam_item(self, item_id: str) -> bool:
        item = self.__koleksi.get(item_id)
        if item is None or not item.pinjam():
            print(f"Item {item_id!r} tidak tersedia untuk dipinjam.")
            return False
        print(f"Item {item_id!r} berhasil dipinjam.")
        return True

    def kembalikan_item(self, item_id: str) -> bool:
        item = self.__koleksi.get(item_id)
        if item is None or not item.kembalikan():
            print(f"Item {item_id!r} tidak tercatat sedang dipinjam.")
            return False
        print(f"Item {item_id!r} berhasil dikembalikan.")
        return True
