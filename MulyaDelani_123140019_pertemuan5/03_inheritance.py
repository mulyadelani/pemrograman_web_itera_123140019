"""Demonstrasi inheritance, method overriding, multiple inheritance, dan MRO."""

if __package__:
    from .kendaraan import Kendaraan
else:
    from kendaraan import Kendaraan


class Mobil(Kendaraan):
    """Kendaraan beroda empat dengan tangki bahan bakar."""

    def __init__(
        self, merek: str, model: str, tahun: int, jumlah_pintu: int, kapasitas_tangki: float
    ) -> None:
        super().__init__(merek, model, tahun)
        self.jumlah_pintu = jumlah_pintu
        self.kapasitas_tangki = kapasitas_tangki
        self.sisa_bensin = kapasitas_tangki

    def deskripsi(self) -> str:
        return (
            f"{super().deskripsi()} [Mobil {self.jumlah_pintu} pintu, "
            f"Tangki: {self.kapasitas_tangki}L]"
        )

    def klakson(self) -> str:
        return "Telolet! Telolet! (Klakson Mobil)"

    def isi_bensin(self, liter: float) -> bool:
        if liter <= 0 or self.sisa_bensin + liter > self.kapasitas_tangki:
            print("Pengisian tidak valid atau kapasitas tangki akan meluap.")
            return False
        self.sisa_bensin += liter
        print(f"[{self.merek} {self.model}] Diisi {liter}L. Sisa: {self.sisa_bensin}L")
        return True


class Motor(Kendaraan):
    """Kendaraan roda dua dengan kapasitas mesin."""

    def __init__(self, merek: str, model: str, tahun: int, kapasitas_cc: int) -> None:
        super().__init__(merek, model, tahun)
        self.kapasitas_cc = kapasitas_cc

    def deskripsi(self) -> str:
        return f"{super().deskripsi()} [Motor {self.kapasitas_cc}cc]"

    def klakson(self) -> str:
        return "Bip bip! (Klakson Motor)"

    def wheelie(self) -> None:
        print(f"[{self.merek} {self.model}] Melakukan atraksi wheelie satu roda!")


class KomponenBaterai:
    """Komponen yang menyimpan kapasitas dan persentase baterai."""

    def __init__(self, kapasitas_kwh: float) -> None:
        self.kapasitas_kwh = kapasitas_kwh
        self.daya_tersisa = 100.0

    def isi_daya(self, persen: float) -> None:
        if persen > 0:
            self.daya_tersisa = min(100.0, self.daya_tersisa + persen)
        print(f"Baterai diisi ulang. Kapasitas daya: {self.daya_tersisa}%")


class MobilListrik(Mobil, KomponenBaterai):
    """Mobil yang mewarisi perilaku kendaraan dan komponen baterai."""

    def __init__(self, merek: str, model: str, tahun: int, kapasitas_kwh: float) -> None:
        Mobil.__init__(self, merek, model, tahun, jumlah_pintu=4, kapasitas_tangki=0.0)
        KomponenBaterai.__init__(self, kapasitas_kwh)

    def deskripsi(self) -> str:
        return (
            f"{self.merek} {self.model} ({self.tahun}) [EV {self.kapasitas_kwh} kWh, "
            f"Daya: {self.daya_tersisa}%]"
        )


if __name__ == "__main__":
    avanza = Mobil("Toyota", "Avanza Veloz", 2023, jumlah_pintu=5, kapasitas_tangki=45.0)
    cbr = Motor("Honda", "CBR250RR", 2022, kapasitas_cc=250)
    ioniq = MobilListrik("Hyundai", "Ioniq 5", 2024, kapasitas_kwh=72.6)

    print("--- Deskripsi Kendaraan ---")
    for kendaraan in (avanza, cbr, ioniq):
        print(kendaraan.deskripsi())
    print("\n--- Polimorfisme Klakson ---")
    for kendaraan in (avanza, cbr):
        print(f"{kendaraan.model}: {kendaraan.klakson()}")

    avanza.tambah_jarak(120.5)
    avanza.isi_bensin(15)
    cbr.wheelie()
    ioniq.isi_daya(30)
    print("\nAvanza adalah Kendaraan:", isinstance(avanza, Kendaraan))
    print("Mobil subclass Kendaraan:", issubclass(Mobil, Kendaraan))
    print("MRO MobilListrik:", [kelas.__name__ for kelas in MobilListrik.__mro__])
