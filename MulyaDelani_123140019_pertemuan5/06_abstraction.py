"""Contoh abstract class, abstract method, dan pola interface."""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Kontrak untuk bangun datar."""

    def __init__(self, nama: str) -> None:
        self.nama = nama

    @abstractmethod
    def luas(self) -> float:
        """Menghitung luas bangun."""

    @abstractmethod
    def keliling(self) -> float:
        """Menghitung keliling bangun."""

    def cetak_laporan(self) -> None:
        print(f"[{self.nama}] Luas: {self.luas():.2f} | Keliling: {self.keliling():.2f}")


class PersegiPanjang(Shape):
    def __init__(self, panjang: float, lebar: float) -> None:
        if panjang <= 0 or lebar <= 0:
            raise ValueError("Panjang dan lebar harus lebih besar dari nol.")
        super().__init__("Persegi Panjang")
        self.panjang = panjang
        self.lebar = lebar

    def luas(self) -> float:
        return self.panjang * self.lebar

    def keliling(self) -> float:
        return 2 * (self.panjang + self.lebar)


class Lingkaran(Shape):
    def __init__(self, radius: float) -> None:
        if radius <= 0:
            raise ValueError("Radius harus lebih besar dari nol.")
        super().__init__("Lingkaran")
        self.radius = radius

    def luas(self) -> float:
        return math.pi * self.radius**2

    def keliling(self) -> float:
        return 2 * math.pi * self.radius


class DatabaseConnector(ABC):
    """Interface konektor database untuk contoh backend."""

    @property
    @abstractmethod
    def driver_name(self) -> str:
        """Nama driver database."""

    @abstractmethod
    def connect(self, host: str, port: int, database: str) -> bool:
        """Membuka koneksi database."""

    @abstractmethod
    def execute_query(self, sql: str) -> list[dict[str, object]]:
        """Menjalankan query simulasi."""

    @abstractmethod
    def disconnect(self) -> None:
        """Menutup koneksi database."""


class PostgreSQLConnector(DatabaseConnector):
    @property
    def driver_name(self) -> str:
        return "PostgreSQL (psycopg2)"

    def connect(self, host: str, port: int, database: str) -> bool:
        print(f"[{self.driver_name}] Terhubung ke {host}:{port}/{database} [OK]")
        return True

    def execute_query(self, sql: str) -> list[dict[str, object]]:
        print(f"[{self.driver_name}] Menjalankan SQL: {sql!r}")
        return [{"id": 1, "nama": "Ahmad"}, {"id": 2, "nama": "Nabila"}]

    def disconnect(self) -> None:
        print(f"[{self.driver_name}] Koneksi ditutup dengan aman.")


class SegitigaCacat(Shape):
    """Contoh subclass tidak valid karena belum mengimplementasikan keliling."""

    def __init__(self, alas: float, tinggi: float) -> None:
        super().__init__("Segitiga Cacat")
        self.alas = alas
        self.tinggi = tinggi

    def luas(self) -> float:
        return 0.5 * self.alas * self.tinggi


if __name__ == "__main__":
    PersegiPanjang(10, 5).cetak_laporan()
    Lingkaran(7).cetak_laporan()

    for kelas in (Shape, SegitigaCacat):
        try:
            kelas("Bentuk Abstrak") if kelas is Shape else kelas(6, 8)
        except TypeError as error:
            print(f"Instansiasi {kelas.__name__} ditolak: {error}")

    db = PostgreSQLConnector()
    db.connect("localhost", 5432, "paw_praktikum_db")
    print("Hasil query:", db.execute_query("SELECT id, nama FROM mahasiswa;"))
    db.disconnect()
