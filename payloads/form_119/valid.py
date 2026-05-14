from payloads.form_119.dictionaries import (
    fields_15804,
    fields_16434,
    fields_20258,
    fields_30973,
    field_date_15803_20544_15878,
    fields_15859,
    fields_15860,
    fields_15861,
    fields_15862,
    fields_15863,
    fields_15864,
    fields_15865,
    fields_15867,
    fields_15868,
    fields_15869,
    fields_15870,
    fields_15916,
    fields_15917,
    fields_16433,
    fields_16567,
    fields_20367,
    fields_20368,
    fields_20369,
    fields_20370,
    fields_20371,
    fields_20372,
    fields_20373,
    fields_20374,
)


def build_form_119_payload() -> dict:
    report_date = field_date_15803_20544_15878()
    registration_date = field_date_15803_20544_15878()
    hospitalization_date = field_date_15803_20544_15878()
    mkb_primary = fields_15804()
    mkb_secondary = fields_16434()
    city = fields_16567()
    localization = fields_15859()
    transmission_path = fields_15916()
    laboratory_confirmed = fields_15917()
    emergency_notice = fields_20258()

    def select_field(field_id: int, item: dict) -> dict:
        return {
            "field_id": field_id,
            "value": [item["name"]],
            "entity": [item["id"]],
            "comments": "",
        }

    data = [
        {"field_id": 15803, "value": report_date, "entity": "", "comments": ""},
        select_field(15804, mkb_primary),
        {"field_id": 20544, "value": registration_date, "entity": "", "comments": ""},
        {"field_id": 15878, "value": hospitalization_date, "entity": "", "comments": ""},
        {"field_id": 30973, "value": fields_30973(), "entity": "", "comments": ""},
        select_field(16434, mkb_secondary),
        select_field(16567, city),
        select_field(15859, localization),
        select_field(15916, transmission_path),
        select_field(15917, laboratory_confirmed),
        select_field(20258, emergency_notice),
        {"field_id": 16433, "value": fields_16433(), "entity": "", "comments": ""},
        {"field_id": 15860, "value": fields_15860(), "entity": "", "comments": ""},
        {"field_id": 20367, "value": fields_20367(), "entity": "", "comments": ""},
        {"field_id": 20368, "value": fields_20368(), "entity": "", "comments": ""},
        {"field_id": 20369, "value": fields_20369(), "entity": "", "comments": ""},
        {"field_id": 20370, "value": fields_20370(), "entity": "", "comments": ""},
        {"field_id": 15862, "value": fields_15862(), "entity": "", "comments": ""},
        {"field_id": 15861, "value": fields_15861(), "entity": "", "comments": ""},
        {"field_id": 15863, "value": fields_15863(), "entity": "", "comments": ""},
        {"field_id": 20371, "value": fields_20371(), "entity": "", "comments": ""},
        {"field_id": 20372, "value": fields_20372(), "entity": "", "comments": ""},
        {"field_id": 20373, "value": fields_20373(), "entity": "", "comments": ""},
        {"field_id": 20374, "value": fields_20374(), "entity": "", "comments": ""},
        {"field_id": 15865, "value": fields_15865(), "entity": "", "comments": ""},
        {"field_id": 15864, "value": fields_15864(), "entity": "", "comments": ""},
        {"field_id": 15870, "value": fields_15870(), "entity": "", "comments": ""},
        {"field_id": 15869, "value": fields_15869(), "entity": "", "comments": ""},
        {"field_id": 15868, "value": fields_15868(), "entity": "", "comments": ""},
        {"field_id": 15867, "value": fields_15867(), "entity": "", "comments": ""},
    ]

    return {
        "anket_type": 119,
        "create_user": 195,
        "is_active": True,
        "attribute": {
            "org_id": 16796,
            "region_id": 77,
        },
        "data": data,
    }
