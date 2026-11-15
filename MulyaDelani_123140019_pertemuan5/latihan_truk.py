"""Latihan subclass Truk yang memvalidasi kapasitas muatan."""

if __package__:
    from .kendaraan import Kendaraan
else:
    from kendaraan import Kendaraan


class Truk(Kendaraan):
    """Kendaraan kargo dengan batas berat muatan."""

    def __init__(
        self,
        merek: str,
        model: str,
        tahun: int,
        kapasitas_maksimal_ton: float,
    ) -> None:
        super().__init__(merek, model, tahun)
        if kapasitas_maksimal_ton <= 0:
            raise ValueError("Kapasitas maksimal harus lebih besar dari nol.")
        self.kapasitas_maksimal_ton = kapasitas_maksimal_ton
        self.muatan_saat_ini = 0.0

    def muat_barang(self, berat_ton: float) -> bool:
        if berat_ton <= 0:
            print("Berat muatan harus lebih besar dari nol.")
            return False
        if self.muatan_saat_ini + berat_ton > self.kapasitas_maksimal_ton:
            print("Muatan melebihi kapasitas maksimal truk.")
            return False
        self.muatan_saat_ini += berat_ton
        print(f"Berhasil memuat {berat_ton} ton.")
        return True

    def deskripsi(self) -> str:
        return (
            f"{super().deskripsi()} [Muatan: {self.muatan_saat_ini}/"
            f"{self.kapasitas_maksimal_ton} ton]"
        )


if __name__ == "__main__":
    truk = Truk("Mitsubishi", "Fuso", 2024, kapasitas_maksimal_ton=8)
    truk.muat_barang(5)
    truk.muat_barang(4)
    print(truk.deskripsi())
