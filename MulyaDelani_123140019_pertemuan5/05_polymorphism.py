"""Contoh polimorfisme pembayaran, duck typing, dan operator overloading."""

from typing import Protocol


class MetodePembayaran:
    """Kontrak sederhana yang harus dipenuhi metode pembayaran."""

    def __init__(self, nama_metode: str) -> None:
        self.nama_metode = nama_metode

    def bayar(self, tagihan: float) -> bool:
        raise NotImplementedError("Subclass wajib mengimplementasikan bayar().")


class BisaBayar(Protocol):
    """Antarmuka struktural untuk semua objek yang dapat memproses pembayaran."""

    def bayar(self, tagihan: float) -> bool:
        """Memproses tagihan."""


class TransferBank(MetodePembayaran):
    def __init__(self, nama_bank: str, nomor_va: str) -> None:
        super().__init__(f"Transfer Bank {nama_bank}")
        self.nomor_va = nomor_va

    def bayar(self, tagihan: float) -> bool:
        biaya_admin = 4000
        total = tagihan + biaya_admin
        print(f"[{self.nama_metode}] Tagihan Rp {tagihan:,.2f} + admin Rp {biaya_admin:,} = Rp {total:,.2f}")
        print(f"Silakan transfer ke Virtual Account: {self.nomor_va}")
        return True


class EWallet(MetodePembayaran):
    def __init__(self, nama_provider: str, nomor_hp: str, saldo_wallet: float) -> None:
        super().__init__(f"E-Wallet {nama_provider}")
        self.nomor_hp = nomor_hp
        self.saldo_wallet = saldo_wallet

    def bayar(self, tagihan: float) -> bool:
        if self.saldo_wallet < tagihan:
            print(f"[{self.nama_metode}] Gagal: saldo Rp {self.saldo_wallet:,.2f} tidak cukup.")
            return False
        self.saldo_wallet -= tagihan
        cashback = tagihan * 0.05
        print(f"[{self.nama_metode}] Pembayaran Rp {tagihan:,.2f} berhasil via {self.nomor_hp}.")
        print(f"Cashback Rp {cashback:,.2f}; sisa saldo Rp {self.saldo_wallet:,.2f}")
        return True


class CryptoPayment:
    """Tidak mewarisi MetodePembayaran; kompatibel lewat duck typing."""

    def __init__(self, wallet_address: str, crypto_symbol: str = "USDT") -> None:
        self.wallet_address = wallet_address
        self.crypto_symbol = crypto_symbol

    def bayar(self, tagihan: float) -> bool:
        total_crypto = tagihan / 16000
        print(f"[Crypto] Rp {tagihan:,.2f} dikonversi menjadi {total_crypto:.2f} {self.crypto_symbol}.")
        print(f"Transaksi simulasi untuk wallet {self.wallet_address[:10]}... berhasil.")
        return True


def proses_checkout_pesanan(daftar_opsi_bayar: list[BisaBayar], total_belanja: float) -> None:
    print(f"\n=== Checkout Rp {total_belanja:,.2f} ===")
    for opsi in daftar_opsi_bayar:
        nama = getattr(opsi, "nama_metode", type(opsi).__name__)
        print(f"\nMemproses opsi: {nama}")
        opsi.bayar(total_belanja)


class Dompet:
    """Nilai saldo yang mendukung operasi tambah dan perbandingan."""

    def __init__(self, pemilik: str, saldo: float) -> None:
        self.pemilik = pemilik
        self.saldo = saldo

    def __add__(self, other: object) -> "Dompet":
        if isinstance(other, Dompet):
            return Dompet(f"{self.pemilik} & {other.pemilik}", self.saldo + other.saldo)
        if isinstance(other, (int, float)):
            return Dompet(self.pemilik, self.saldo + other)
        return NotImplemented

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Dompet):
            return self.saldo == other.saldo
        return False

    def __str__(self) -> str:
        return f"Dompet({self.pemilik}): Rp {self.saldo:,.2f}"


if __name__ == "__main__":
    opsi_pembayaran = [
        TransferBank("BCA", "880121140001"),
        EWallet("GoPay", "081234567890", saldo_wallet=500000),
        CryptoPayment("0x71C...b89A", "USDT"),
    ]
    proses_checkout_pesanan(opsi_pembayaran, 320000)

    print("\n--- Operator Overloading ---")
    d1 = Dompet("Andi", 150000)
    d2 = Dompet("Budi", 250000)
    print("Dompet 1:", d1)
    print("Dompet 2:", d2)
    print("Gabungan:", d1 + d2)
    print("Saldo sama:", d1 == d2)
