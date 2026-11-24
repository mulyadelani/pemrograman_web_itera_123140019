import pytest

from pyramid_mahasiswa.validation import validate_matakuliah_payload


def test_valid_course_payload_is_normalized():
    values, error = validate_matakuliah_payload(
        {
            "kode_mk": " IF2110 ",
            "nama_mk": " Pemrograman Web ",
            "sks": 3,
            "semester": 5,
        }
    )

    assert error is None
    assert values == {
        "kode_mk": "IF2110",
        "nama_mk": "Pemrograman Web",
        "sks": 3,
        "semester": 5,
    }


@pytest.mark.parametrize(
    ("payload", "message"),
    [
        ({"nama_mk": "Basis Data", "sks": 3, "semester": 5}, "kode_mk"),
        ({"kode_mk": "IF1", "nama_mk": "Basis Data", "sks": 0, "semester": 5}, "sks"),
        (
            {"kode_mk": "IF1", "nama_mk": "Basis Data", "sks": 3, "semester": -1},
            "semester",
        ),
        (
            {"kode_mk": "IF1", "nama_mk": "Basis Data", "sks": True, "semester": 5},
            "sks",
        ),
    ],
)
def test_invalid_course_payload_is_rejected(payload, message):
    values, error = validate_matakuliah_payload(payload)

    assert values is None
    assert message in error


def test_partial_update_requires_at_least_one_valid_field():
    values, error = validate_matakuliah_payload({}, partial=True)

    assert values is None
    assert "minimal satu field" in error
