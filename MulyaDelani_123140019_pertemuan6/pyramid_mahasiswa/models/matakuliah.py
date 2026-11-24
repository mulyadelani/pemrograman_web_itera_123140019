from sqlalchemy import CheckConstraint, Integer, Text
from sqlalchemy.orm import Mapped, mapped_column

from .meta import Base


class Matakuliah(Base):
    """Data mata kuliah dengan SKS dan semester bernilai positif."""

    __tablename__ = "matakuliah"
    __table_args__ = (
        CheckConstraint("sks > 0", name="ck_matakuliah_sks_positive"),
        CheckConstraint("semester > 0", name="ck_matakuliah_semester_positive"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    kode_mk: Mapped[str] = mapped_column(Text, unique=True, nullable=False)
    nama_mk: Mapped[str] = mapped_column(Text, nullable=False)
    sks: Mapped[int] = mapped_column(Integer, nullable=False)
    semester: Mapped[int] = mapped_column(Integer, nullable=False)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "kode_mk": self.kode_mk,
            "nama_mk": self.nama_mk,
            "sks": self.sks,
            "semester": self.semester,
        }
