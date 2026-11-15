"""Latihan class Buku dengan diskon dan dunder method __len__."""


class Buku:
    """Menyimpan informasi buku dan menghitung harga setelah diskon."""

    def __init__(self, judul: str, penulis: str, harga_asli: float, jumlah_halaman: int) -> None:
        if harga_asli < 0 or jumlah_halaman < 0:
            raise ValueError("Harga dan jumlah halaman tidak boleh negatif.")
        self.judul = judul
        self.penulis = penulis
        self.harga_asli = harga_asli
        self.jumlah_halaman = jumlah_halaman

    def hitung_harga_diskon(self, persen: float) -> float:
        if not 0 <= persen <= 100:
            raise ValueError("Diskon harus berada pada rentang 0 sampai 100 persen.")
        return self.harga_asli * (1 - persen / 100)

    def __len__(self) -> int:
        return self.jumlah_halaman

    def __str__(self) -> str:
        return (
            f"Kartu Buku: {self.judul} oleh {self.penulis} | "
            f"Harga: Rp {self.harga_asli:,.0f} | Halaman: {len(self)}"
        )


if __name__ == "__main__":
    buku = Buku("Belajar OOP Python", "Mulya Delani", 120000, 240)
    print(buku)
    print(f"Harga setelah diskon 15%: Rp {buku.hitung_harga_diskon(15):,.0f}")
