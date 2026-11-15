"""Abstract item dan implementasi buku serta majalah."""

from abc import ABC, abstractmethod


class LibraryItem(ABC):
    """Kelas dasar item perpustakaan dengan status peminjaman terlindungi."""

    def __init__(self, item_id: str, judul: str) -> None:
        if not item_id.strip() or not judul.strip():
            raise ValueError("ID dan judul item wajib diisi.")
        self._item_id = item_id.strip()
        self._judul = judul.strip()
        self.__dipinjam = False

    @property
    def item_id(self) -> str:
        return self._item_id

    @property
    def judul(self) -> str:
        return self._judul

    @property
    def is_dipinjam(self) -> bool:
        return self.__dipinjam

    def pinjam(self) -> bool:
        if self.__dipinjam:
            return False
        self.__dipinjam = True
        return True

    def kembalikan(self) -> bool:
        if not self.__dipinjam:
            return False
        self.__dipinjam = False
        return True

    @abstractmethod
    def get_detail(self) -> str:
        """Menghasilkan detail sesuai jenis item."""


class Book(LibraryItem):
    """Item buku dengan nama penulis dan jumlah halaman."""

    def __init__(self, item_id: str, judul: str, penulis: str, jumlah_halaman: int) -> None:
        super().__init__(item_id, judul)
        if jumlah_halaman <= 0:
            raise ValueError("Jumlah halaman buku harus lebih besar dari nol.")
        self.penulis = penulis
        self.jumlah_halaman = jumlah_halaman

    def get_detail(self) -> str:
        return f"Buku: {self.judul} | Penulis: {self.penulis} | {self.jumlah_halaman} halaman"


class Magazine(LibraryItem):
    """Item majalah dengan nomor edisi dan bulan terbit."""

    def __init__(self, item_id: str, judul: str, edisi: int, bulan_terbit: str) -> None:
        super().__init__(item_id, judul)
        if edisi <= 0:
            raise ValueError("Nomor edisi harus lebih besar dari nol.")
        self.edisi = edisi
        self.bulan_terbit = bulan_terbit

    def get_detail(self) -> str:
        return f"Majalah: {self.judul} | Edisi {self.edisi} | Terbit: {self.bulan_terbit}"
