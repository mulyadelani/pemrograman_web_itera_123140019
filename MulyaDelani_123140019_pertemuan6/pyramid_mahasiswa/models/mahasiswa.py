from datetime import date

from sqlalchemy import Date, Integer, Text
from sqlalchemy.orm import Mapped, mapped_column

from .meta import Base


class Mahasiswa(Base):
    """Data mahasiswa yang disimpan pada tabel mahasiswa."""

    __tablename__ = "mahasiswa"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nim: Mapped[str] = mapped_column(Text, unique=True, nullable=False)
    nama: Mapped[str] = mapped_column(Text, nullable=False)
    jurusan: Mapped[str] = mapped_column(Text, nullable=False)
    tanggal_lahir: Mapped[date | None] = mapped_column(Date, nullable=True)
    alamat: Mapped[str | None] = mapped_column(Text, nullable=True)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "nim": self.nim,
            "nama": self.nama,
            "jurusan": self.jurusan,
            "tanggal_lahir": (
                self.tanggal_lahir.isoformat() if self.tanggal_lahir else None
            ),
            "alamat": self.alamat,
        }
