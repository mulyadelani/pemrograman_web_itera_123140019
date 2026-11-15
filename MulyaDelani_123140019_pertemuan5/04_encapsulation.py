"""Contoh encapsulation, name mangling, dan property pada rekening bank."""


class RekeningBank:
    """Rekening dengan saldo dan PIN yang dilindungi."""

    def __init__(self, nomor_rekening: str, nama_pemilik: str, saldo_awal: float, pin: str) -> None:
        self.nomor_rekening = nomor_rekening
        self._pemilik = nama_pemilik
        self.__saldo = max(0.0, float(saldo_awal))
        self.__pin = str(pin)
        self._riwayat_transaksi: list[str] = []

    @property
    def saldo(self) -> float:
        """Membaca saldo tanpa memberi akses langsung ke atribut internal."""
        return self.__saldo

    @saldo.setter
    def saldo(self, jumlah_baru: float) -> None:
        if not isinstance(jumlah_baru, (int, float)):
            raise TypeError("Nilai saldo harus berupa angka numerik.")
        if jumlah_baru < 0:
            raise ValueError("Saldo rekening tidak boleh bernilai negatif.")
        self.__saldo = float(jumlah_baru)
        print(f"[AUDIT] Saldo {self.nomor_rekening} disesuaikan menjadi Rp {self.__saldo:,.2f}")

    def setor(self, nominal: float) -> bool:
        if nominal <= 0:
            print("Gagal: nominal setor harus lebih besar dari Rp 0.")
            return False
        self.__saldo += nominal
        self._riwayat_transaksi.append(f"Setor Tunai: +Rp {nominal:,.2f}")
        print(f"Setor tunai Rp {nominal:,.2f} sukses. Saldo: Rp {self.__saldo:,.2f}")
        return True

    def tarik(self, nominal: float, pin_input: str) -> bool:
        if pin_input != self.__pin:
            print("Gagal: PIN transaksi salah.")
            return False
        if nominal <= 0:
            print("Gagal: nominal penarikan harus lebih dari Rp 0.")
            return False
        if nominal > self.__saldo:
            print(f"Gagal: saldo tidak mencukupi (Rp {self.__saldo:,.2f}).")
            return False
        self.__saldo -= nominal
        self._riwayat_transaksi.append(f"Tarik Tunai: -Rp {nominal:,.2f}")
        print(f"Tarik tunai Rp {nominal:,.2f} berhasil. Sisa saldo: Rp {self.__saldo:,.2f}")
        return True

    def cetak_mutasi(self) -> None:
        print(f"\n=== MUTASI {self.nomor_rekening} ({self._pemilik}) ===")
        for transaksi in self._riwayat_transaksi:
            print(" -", transaksi)
        print(f"Saldo akhir: Rp {self.__saldo:,.2f}")


if __name__ == "__main__":
    rekening = RekeningBank("121-009-8871", "Ahmad Fadhilah", 500000, "123456")
    print("Nomor rekening:", rekening.nomor_rekening)
    print("Pemilik:", rekening._pemilik)
    print(f"Saldo: Rp {rekening.saldo:,.2f}")

    rekening.setor(250000)
    rekening.tarik(100000, "999999")
    rekening.tarik(100000, "123456")
    rekening.tarik(1000000, "123456")
    try:
        rekening.saldo = -50000
    except ValueError as error:
        print(f"\nValidasi tertangkap: {error}")
    try:
        print(rekening.__saldo)
    except AttributeError:
        print("Akses langsung rekening.__saldo gagal karena name mangling.")
    rekening.cetak_mutasi()
