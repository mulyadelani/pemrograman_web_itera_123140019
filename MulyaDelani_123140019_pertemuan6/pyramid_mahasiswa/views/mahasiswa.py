from datetime import date

from pyramid.httpexceptions import HTTPBadRequest, HTTPNotFound
from pyramid.view import view_config

from ..models import Mahasiswa
from .helpers import json_object_body


@view_config(route_name="mahasiswa_list", renderer="json")
def mahasiswa_list(request):
    records = (
        request.dbsession.query(Mahasiswa)
        .order_by(Mahasiswa.id.asc())
        .all()
    )
    return {"mahasiswas": [record.to_dict() for record in records]}


@view_config(route_name="mahasiswa_detail", renderer="json")
def mahasiswa_detail(request):
    record = request.dbsession.get(Mahasiswa, int(request.matchdict["id"]))
    if record is None:
        return HTTPNotFound(
            json_body={
                "error": (
                    f"Mahasiswa dengan ID {request.matchdict['id']} "
                    "tidak ditemukan"
                )
            }
        )
    return {"mahasiswa": record.to_dict()}


@view_config(route_name="mahasiswa_add", request_method="POST", renderer="json")
def mahasiswa_add(request):
    data, error = json_object_body(request)
    if error:
        return error

    for field in ("nim", "nama", "jurusan"):
        if not isinstance(data.get(field), str) or not data[field].strip():
            return HTTPBadRequest(json_body={"error": f"Field {field} wajib diisi!"})

    tanggal_lahir = None
    if data.get("tanggal_lahir"):
        try:
            tanggal_lahir = date.fromisoformat(data["tanggal_lahir"])
        except (TypeError, ValueError):
            return HTTPBadRequest(
                json_body={
                    "error": (
                        "Format tanggal lahir tidak valid. Gunakan YYYY-MM-DD."
                    )
                }
            )

    dbsession = request.dbsession
    if dbsession.query(Mahasiswa).filter_by(nim=data["nim"].strip()).first():
        return HTTPBadRequest(json_body={"error": "NIM sudah terdaftar."})

    record = Mahasiswa(
        nim=data["nim"].strip(),
        nama=data["nama"].strip(),
        jurusan=data["jurusan"].strip(),
        tanggal_lahir=tanggal_lahir,
        alamat=data.get("alamat"),
    )
    dbsession.add(record)
    dbsession.flush()
    return {"success": True, "mahasiswa": record.to_dict()}


@view_config(route_name="mahasiswa_update", request_method="PUT", renderer="json")
def mahasiswa_update(request):
    dbsession = request.dbsession
    record = dbsession.get(Mahasiswa, int(request.matchdict["id"]))
    if record is None:
        return HTTPNotFound(
            json_body={
                "error": (
                    f"Mahasiswa dengan ID {request.matchdict['id']} "
                    "tidak ditemukan"
                )
            }
        )

    data, error = json_object_body(request)
    if error:
        return error
    for field in ("nim", "nama", "jurusan"):
        if field in data:
            if not isinstance(data[field], str) or not data[field].strip():
                return HTTPBadRequest(
                    json_body={"error": f"Field {field} tidak boleh kosong."}
                )
            setattr(record, field, data[field].strip())
    if "alamat" in data:
        record.alamat = data["alamat"]
    if "tanggal_lahir" in data:
        try:
            record.tanggal_lahir = (
                date.fromisoformat(data["tanggal_lahir"])
                if data["tanggal_lahir"]
                else None
            )
        except (TypeError, ValueError):
            return HTTPBadRequest(
                json_body={
                    "error": (
                        "Format tanggal lahir tidak valid. Gunakan YYYY-MM-DD."
                    )
                }
            )
    if "nim" in data:
        duplicate = (
            dbsession.query(Mahasiswa)
            .filter(Mahasiswa.nim == record.nim, Mahasiswa.id != record.id)
            .first()
        )
        if duplicate:
            return HTTPBadRequest(json_body={"error": "NIM sudah terdaftar."})
    return {"success": True, "mahasiswa": record.to_dict()}


@view_config(route_name="mahasiswa_delete", request_method="DELETE", renderer="json")
def mahasiswa_delete(request):
    dbsession = request.dbsession
    record = dbsession.get(Mahasiswa, int(request.matchdict["id"]))
    if record is None:
        return HTTPNotFound(
            json_body={
                "error": (
                    f"Mahasiswa dengan ID {request.matchdict['id']} "
                    "tidak ditemukan"
                )
            }
        )
    dbsession.delete(record)
    return {
        "success": True,
        "message": f"Mahasiswa dengan ID {record.id} berhasil dihapus",
    }
