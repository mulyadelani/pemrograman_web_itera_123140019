"""Latihan pemodelan entitas Produk, Keranjang, dan Pengguna."""


class Produk:
    """Produk memiliki nama, harga, stok; perilakunya mengubah dan memeriksa stok."""

    def __init__(self, nama: str, harga: float, stok: int) -> None:
        self.nama = nama
        self.harga = harga
        self.stok = stok

    def cek_ketersediaan(self, jumlah: int) -> bool:
        return 0 < jumlah <= self.stok

    def kurangi_stok(self, jumlah: int) -> bool:
        if not self.cek_ketersediaan(jumlah):
            return False
        self.stok -= jumlah
        return True


class Keranjang:
    """Keranjang menyimpan pemilik, daftar produk, dan total belanja."""

    def __init__(self, pemilik: str) -> None:
        self.pemilik = pemilik
        self.daftar_produk: list[tuple[Produk, int]] = []
        self.total_belanja = 0.0

    def tambah_produk(self, produk: Produk, jumlah: int) -> bool:
        if not produk.cek_ketersediaan(jumlah):
            return False
        self.daftar_produk.append((produk, jumlah))
        self.total_belanja += produk.harga * jumlah
        return True

    def kosongkan(self) -> None:
        self.daftar_produk.clear()
        self.total_belanja = 0.0


class Pengguna:
    """Pengguna memiliki identitas dan informasi kontak."""

    def __init__(self, nama: str, email: str, alamat: str) -> None:
        self.nama = nama
        self.email = email
        self.alamat = alamat

    def perbarui_alamat(self, alamat_baru: str) -> None:
        self.alamat = alamat_baru

    def buat_keranjang(self) -> Keranjang:
        return Keranjang(self.nama)


if __name__ == "__main__":
    pengguna = Pengguna("Mulya Delani", "mulya@example.com", "Lampung")
    produk = Produk("Buku OOP", 75000, 10)
    keranjang = pengguna.buat_keranjang()
    keranjang.tambah_produk(produk, 2)
    print("Atribut Produk: nama, harga, stok")
    print("Metode Produk: cek_ketersediaan(), kurangi_stok()")
    print("Atribut Keranjang: pemilik, daftar_produk, total_belanja")
    print("Metode Keranjang: tambah_produk(), kosongkan()")
    print("Atribut Pengguna: nama, email, alamat")
    print("Metode Pengguna: perbarui_alamat(), buat_keranjang()")
    print(f"Total belanja {keranjang.pemilik}: Rp {keranjang.total_belanja:,.0f}")
