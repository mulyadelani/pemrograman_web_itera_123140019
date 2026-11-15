"""Kelas dasar kendaraan yang dipakai dalam hands-on dan latihan truk."""


class Kendaraan:
    """Data dan perilaku umum kendaraan."""

    def __init__(self, merek: str, model: str, tahun: int) -> None:
        self.merek = merek
        self.model = model
        self.tahun = tahun
        self.odometer = 0.0

    def deskripsi(self) -> str:
        return f"{self.merek} {self.model} ({self.tahun})"

    def tambah_jarak(self, km: float) -> None:
        if km <= 0:
            print("Nilai kilometer tambahan tidak valid.")
            return
        self.odometer += km
        print(f"[{self.merek}] Menempuh +{km} km. Total odometer: {self.odometer} km")

    def klakson(self) -> str:
        return "Tin tin!"
