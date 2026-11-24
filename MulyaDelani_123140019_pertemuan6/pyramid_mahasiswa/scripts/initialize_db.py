import argparse
import sys
from datetime import date

from pyramid.paster import bootstrap, setup_logging
from sqlalchemy.exc import OperationalError

from ..models import Mahasiswa, Matakuliah


def setup_models(dbsession):
    """Seed mahasiswa dan mata kuliah tanpa menggandakan data unik."""
    if not dbsession.query(Mahasiswa).filter_by(nim="12345").first():
        dbsession.add(
            Mahasiswa(
                nim="12345",
                nama="Budi Santoso",
                jurusan="Teknik Informatika",
                tanggal_lahir=date(2000, 5, 15),
                alamat="Bandung",
            )
        )
    if not dbsession.query(Mahasiswa).filter_by(nim="54321").first():
        dbsession.add(
            Mahasiswa(
                nim="54321",
                nama="Siti Aminah",
                jurusan="Sistem Informasi",
                tanggal_lahir=date(2001, 8, 22),
                alamat="Jakarta",
            )
        )

    seed_courses = (
        ("IF2110", "Pemrograman Web", 3, 5),
        ("IF3140", "Basis Data", 4, 5),
        ("IF2120", "Struktur Data", 3, 3),
    )
    for kode_mk, nama_mk, sks, semester in seed_courses:
        if not dbsession.query(Matakuliah).filter_by(kode_mk=kode_mk).first():
            dbsession.add(
                Matakuliah(
                    kode_mk=kode_mk,
                    nama_mk=nama_mk,
                    sks=sks,
                    semester=semester,
                )
            )


def parse_args(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("config_uri", help="Configuration file, e.g. development.ini")
    return parser.parse_args(argv[1:])


def main(argv=sys.argv):
    args = parse_args(argv)
    setup_logging(args.config_uri)
    env = bootstrap(args.config_uri)
    try:
        with env["request"].tm:
            setup_models(env["request"].dbsession)
        print("Berhasil memasukkan data awal mahasiswa dan mata kuliah.")
    except OperationalError as error:
        print(f"Gagal terhubung ke database: {error}", file=sys.stderr)
        raise
    finally:
        env["closer"]()


if __name__ == "__main__":
    main()
