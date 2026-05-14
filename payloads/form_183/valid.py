import random

from payloads.form_183.dictionaries import (
    RESEARCH_COMPLETED,
    get_random_research_completed,
    get_random_reserch_client,
    get_random_source_of_selection,
    get_random_research_method,
    get_random_taxonomic_items,
    get_random_external_lab,
)


EXTERNAL_LAB_RESEARCH_COMPLETED_ID = RESEARCH_COMPLETED[0]["id"]


def build_form_183_payload():
    random_date = (
        f"{random.randint(2023, 2026)}-"
        f"{random.randint(1, 12):02d}-"
        f"{random.randint(1, 28):02d}"
    )
    research_completed = get_random_research_completed()
    external_lab_name = get_random_external_lab()
    research_client = get_random_reserch_client()
    source_of_selection = get_random_source_of_selection()
    research_method = get_random_research_method()
    taxonomic_items = get_random_taxonomic_items()

    def select_field(field_id: int, item: dict) -> dict:
        return {
            "field_id": field_id,
            "value": [item["name"]],
            "entity": [item["id"]],
            "comments": "",
        }

    data = [
        select_field(21684, research_completed),
        select_field(21685, research_client),
        select_field(21686, research_client),
        {"field_id": 21677, "value": random.choice(["ИВР", "ПЕТ", "СИД", "МИХ"]), "entity": "", "comments": ""},
        {"field_id": 21678, "value": random_date, "entity": "", "comments": ""},
        {"field_id": 21680, "value": random_date, "entity": "", "comments": ""},
        {"field_id": 21681, "value": random_date, "entity": "", "comments": ""},
        select_field(21682, taxonomic_items),
        select_field(21687, source_of_selection),
        select_field(21690, research_method),
        {"field_id": 21688, "value": random.choice(["Примечание раз два три четыре", "Возможно тут будет ваша реклама"]), "entity": "", "comments": ""},
    ]

    if research_completed["id"] == EXTERNAL_LAB_RESEARCH_COMPLETED_ID:
        data.insert(1, select_field(21683, external_lab_name))

    return {
        "anket_type": 183,
        "create_user": 195,
        "is_active": True,
        "attribute": {
            "org_id": 16796,
            "region_id": 77,
        },
        "data": data,
    }
