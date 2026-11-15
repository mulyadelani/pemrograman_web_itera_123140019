"""Membandingkan pendekatan prosedural dan berorientasi objek."""


mahasiswa_proc = {
    "nama": "Budi Santoso",
    "nim": "121140001",
    "jurusan": "Teknik Informatika",
    "ipk": 3.45,
}


def cetak_profil_prosedural(mahasiswa: dict[str, object]) -> None:
    print(
        f"[Prosedural] {mahasiswa['nama']} ({mahasiswa['nim']}) - "
        f"{mahasiswa['jurusan']} | IPK: {mahasiswa['ipk']}"
    )


def perbarui_ipk_prosedural(mahasiswa: dict[str, object], ipk_baru: float) -> None:
    if 0.0 <= ipk_baru <= 4.0:
        mahasiswa["ipk"] = ipk_baru
    else:
        print("Peringatan: IPK harus berada pada rentang 0.0 sampai 4.0.")


class Mahasiswa:
    """Menyimpan data mahasiswa dan perilaku yang terkait."""

    def __init__(self, nama: str, nim: str, jurusan: str, ipk: float) -> None:
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.ipk = ipk

    def cetak_profil(self) -> None:
        print(f"[OOP] {self.nama} ({self.nim}) - {self.jurusan} | IPK: {self.ipk}")

    def update_ipk(self, ipk_baru: float) -> None:
        if 0.0 <= ipk_baru <= 4.0:
            self.ipk = ipk_baru
            print(f"IPK {self.nama} berhasil diperbarui menjadi {self.ipk}.")
        else:
            print("Peringatan: IPK harus berada pada rentang 0.0 sampai 4.0.")


if __name__ == "__main__":
    print("--- Pendekatan Prosedural ---")
    cetak_profil_prosedural(mahasiswa_proc)
    perbarui_ipk_prosedural(mahasiswa_proc, 3.75)
    cetak_profil_prosedural(mahasiswa_proc)

    print("\n--- Pendekatan OOP ---")
    mahasiswa = Mahasiswa("Siti Rahma", "121140002", "Teknik Informatika", 3.80)
    mahasiswa.cetak_profil()
    mahasiswa.update_ipk(3.92)
    mahasiswa.cetak_profil()
