from pyramid.httpexceptions import HTTPBadRequest


def json_object_body(request):
    try:
        payload = request.json_body
    except (ValueError, UnicodeDecodeError):
        return None, HTTPBadRequest(
            json_body={"error": "Body harus berisi JSON yang valid."}
        )
    if not isinstance(payload, dict):
        return None, HTTPBadRequest(
            json_body={"error": "Body harus berupa objek JSON."}
        )
    return payload, None
