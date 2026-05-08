import random

from payloads.form_116.valid import build_form_116_payload


def build_form_116_without_data_payload():
    payload = build_form_116_payload()
    payload.pop("data", None)
    return payload


def build_form_116_with_invalid_data_type_payload():
    payload = build_form_116_payload()
    payload["data"] = "invalid-data"
    return payload


def build_form_116_with_invalid_field_id_payload():
    payload = build_form_116_payload()
    payload["anket_type"] = "116"
    payload["data"][0]["field_id"] = "not-an-int"
    return payload


INVALID_FORM_116_BUILDERS = [
    build_form_116_without_data_payload,
    build_form_116_with_invalid_data_type_payload,
    build_form_116_with_invalid_field_id_payload,
]


def build_random_invalid_form_116_payload():
    builder = random.choice(INVALID_FORM_116_BUILDERS)
    return builder()
