from pyramid.httpexceptions import HTTPBadRequest, HTTPNotFound
from pyramid.view import view_config

from ..models import Matakuliah
from ..validation import validate_matakuliah_payload
from .helpers import json_object_body


@view_config(route_name="matakuliah_list", renderer="json")
def matakuliah_list(request):
    records = (
        request.dbsession.query(Matakuliah)
        .order_by(Matakuliah.id.asc())
        .all()
    )
    return {"matakuliahs": [record.to_dict() for record in records]}


@view_config(route_name="matakuliah_detail", renderer="json")
def matakuliah_detail(request):
    record = request.dbsession.get(Matakuliah, int(request.matchdict["id"]))
    if record is None:
        return HTTPNotFound(
            json_body={
                "error": (
                    f"Mata kuliah dengan ID {request.matchdict['id']} "
                    "tidak ditemukan"
                )
            }
        )
    return {"matakuliah": record.to_dict()}


@view_config(route_name="matakuliah_add", request_method="POST", renderer="json")
def matakuliah_add(request):
    data, error = json_object_body(request)
    if error:
        return error
    values, validation_error = validate_matakuliah_payload(data)
    if validation_error:
        return HTTPBadRequest(json_body={"error": validation_error})

    dbsession = request.dbsession
    if dbsession.query(Matakuliah).filter_by(kode_mk=values["kode_mk"]).first():
        return HTTPBadRequest(json_body={"error": "Kode mata kuliah sudah terdaftar."})

    record = Matakuliah(**values)
    dbsession.add(record)
    dbsession.flush()
    return {"success": True, "matakuliah": record.to_dict()}


@view_config(route_name="matakuliah_update", request_method="PUT", renderer="json")
def matakuliah_update(request):
    dbsession = request.dbsession
    record = dbsession.get(Matakuliah, int(request.matchdict["id"]))
    if record is None:
        return HTTPNotFound(
            json_body={
                "error": (
                    f"Mata kuliah dengan ID {request.matchdict['id']} "
                    "tidak ditemukan"
                )
            }
        )

    data, error = json_object_body(request)
    if error:
        return error
    values, validation_error = validate_matakuliah_payload(data, partial=True)
    if validation_error:
        return HTTPBadRequest(json_body={"error": validation_error})

    if "kode_mk" in values:
        duplicate = (
            dbsession.query(Matakuliah)
            .filter(
                Matakuliah.kode_mk == values["kode_mk"],
                Matakuliah.id != record.id,
            )
            .first()
        )
        if duplicate:
            return HTTPBadRequest(
                json_body={"error": "Kode mata kuliah sudah terdaftar."}
            )

    for field, value in values.items():
        setattr(record, field, value)
    return {"success": True, "matakuliah": record.to_dict()}


@view_config(route_name="matakuliah_delete", request_method="DELETE", renderer="json")
def matakuliah_delete(request):
    dbsession = request.dbsession
    record = dbsession.get(Matakuliah, int(request.matchdict["id"]))
    if record is None:
        return HTTPNotFound(
            json_body={
                "error": (
                    f"Mata kuliah dengan ID {request.matchdict['id']} "
                    "tidak ditemukan"
                )
            }
        )
    dbsession.delete(record)
    return {
        "success": True,
        "message": f"Mata kuliah dengan ID {record.id} berhasil dihapus",
    }
