from collections.abc import Mapping


COURSE_FIELDS = ("kode_mk", "nama_mk", "sks", "semester")


def validate_matakuliah_payload(data, partial=False):
    """Return normalized fields or a human-readable validation error."""
    if not isinstance(data, Mapping):
        return None, "Body harus berupa objek JSON."

    if partial and not any(field in data for field in COURSE_FIELDS):
        return None, "Isi minimal satu field yang akan diperbarui."

    normalized = {}
    for field in COURSE_FIELDS:
        if field not in data:
            if not partial:
                return None, f"Field {field} wajib diisi!"
            continue

        value = data[field]
        if field in ("kode_mk", "nama_mk"):
            if not isinstance(value, str) or not value.strip():
                return None, f"Field {field} harus berupa teks dan tidak boleh kosong."
            normalized[field] = value.strip()
            continue

        if type(value) is not int or value <= 0:
            return None, f"Field {field} harus berupa bilangan bulat positif."
        normalized[field] = value

    return normalized, None
