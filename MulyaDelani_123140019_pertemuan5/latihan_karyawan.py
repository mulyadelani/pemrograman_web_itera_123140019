"""Latihan enkapsulasi gaji karyawan dengan property dan validasi UMR."""


class Karyawan:
    """Menyimpan data karyawan dan menghitung gaji bersih setelah pajak."""

    UMR_MINIMUM = 3_200_000

    def __init__(self, nama: str, jabatan: str, gaji_pokok: float) -> None:
        self.nama = nama
        self.jabatan = jabatan
        self.__gaji_pokok = 0.0
        self.gaji_pokok = gaji_pokok

    @property
    def gaji_pokok(self) -> float:
        return self.__gaji_pokok

    @gaji_pokok.setter
    def gaji_pokok(self, nominal: float) -> None:
        if not isinstance(nominal, (int, float)):
            raise TypeError("Gaji pokok harus berupa angka.")
        if nominal < self.UMR_MINIMUM:
            raise ValueError(f"Gaji pokok minimal Rp {self.UMR_MINIMUM:,.0f}.")
        self.__gaji_pokok = float(nominal)

    def hitung_gaji_bersih(self, pajak_persen: float) -> float:
        if not 0 <= pajak_persen <= 100:
            raise ValueError("Pajak harus berada pada rentang 0 sampai 100 persen.")
        return self.gaji_pokok * (1 - pajak_persen / 100)


if __name__ == "__main__":
    karyawan = Karyawan("Mulya Delani", "Programmer", 5_000_000)
    print(f"{karyawan.nama} - {karyawan.jabatan}")
    print(f"Gaji pokok: Rp {karyawan.gaji_pokok:,.0f}")
    print(f"Gaji bersih setelah pajak 5%: Rp {karyawan.hitung_gaji_bersih(5):,.0f}")
    try:
        karyawan.gaji_pokok = 3_000_000
    except ValueError as error:
        print("Validasi tertangkap:", error)
