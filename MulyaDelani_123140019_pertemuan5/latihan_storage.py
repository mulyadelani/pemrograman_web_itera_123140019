"""Latihan abstract class penyimpanan file lokal dan cloud (simulasi)."""

from abc import ABC, abstractmethod


class FileStorage(ABC):
    """Kontrak layanan untuk mengunggah dan mengunduh file."""

    @abstractmethod
    def upload_file(self, nama_file: str, data_bytes: bytes) -> bool:
        """Menyimpan data file dan melaporkan keberhasilan."""

    @abstractmethod
    def download_file(self, nama_file: str) -> bytes | None:
        """Mengambil data file atau None jika file tidak ada."""


class LocalDiskStorage(FileStorage):
    """Simulasi penyimpanan lokal menggunakan dictionary di memori."""

    def __init__(self) -> None:
        self._files: dict[str, bytes] = {}

    def upload_file(self, nama_file: str, data_bytes: bytes) -> bool:
        self._files[nama_file] = data_bytes
        print(f"[Lokal] File {nama_file} tersimpan ({len(data_bytes)} byte).")
        return True

    def download_file(self, nama_file: str) -> bytes | None:
        return self._files.get(nama_file)


class CloudStorage(FileStorage):
    """Simulasi penyimpanan cloud menggunakan dictionary di memori."""

    def __init__(self) -> None:
        self._objects: dict[str, bytes] = {}

    def upload_file(self, nama_file: str, data_bytes: bytes) -> bool:
        self._objects[nama_file] = data_bytes
        print(f"[Cloud] File {nama_file} diunggah ({len(data_bytes)} byte).")
        return True

    def download_file(self, nama_file: str) -> bytes | None:
        return self._objects.get(nama_file)


if __name__ == "__main__":
    for storage in (LocalDiskStorage(), CloudStorage()):
        storage.upload_file("catatan.txt", b"Latihan OOP pertemuan 5")
        hasil = storage.download_file("catatan.txt")
        print(f"Data yang diunduh: {hasil!r}")
