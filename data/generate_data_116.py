    # data/payload_116.py
import random
from datetime import datetime

from data.data_for_fields import (
    get_random_mkb,
    get_random_gender,
    get_random_yes_no,
    get_random_decreted_worker,
    get_random_previous_illness,
    get_random_observation_type,
    get_random_severity,
    get_random_clinical_form,
    get_random_atypical_form,
    get_random_emergency_prevention,
    get_random_travel_status,
    get_random_outcome,
)


def generate_form_116_full():
    """Генерирует полный динамический payload для формы 116"""

    today = datetime.now().date().isoformat()
    birth_year = random.randint(1950, 2020)
    random_date = f"{random.randint(2023, 2026)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"
    random_bool = random.choice([True, False])

    # Выбираем случайные значения из справочников
    mkb_item = get_random_mkb()
    gender_item = get_random_gender()
    yes_no_item = get_random_yes_no()
    decreted_item = get_random_decreted_worker()
    previous_illness_item = get_random_previous_illness()
    observation_item = get_random_observation_type()
    severity_item = get_random_severity()
    clinical_item = get_random_clinical_form()
    atypical_item = get_random_atypical_form()
    emergency_item = get_random_emergency_prevention()
    travel_item = get_random_travel_status()
    outcome_item = get_random_outcome()

    return {
        "anket_type": 116,
        "create_user": 195,
        "is_active": True,
        "attribute": {
          "org_id": 16796,
          "region_id": 77
        },
        "data": [
            # Паспортная часть
            {"field_id": 15614, "value": random.choice(["ИВР", "ПЕТ", "СИД", "МИХ"]), "entity": "", "comments": ""},
            {"field_id": 15615, "value": f"{birth_year}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}",
             "entity": "", "comments": ""},
            {"field_id": 15645, "value": f"{random.choice(['ABC', 'DEF'])}{birth_year}", "entity": "", "comments": ""},

            # Диагнозы (МКБ)
            {"field_id": 15621, "value": [mkb_item["name"]], "entity": [mkb_item["id"]], "comments": ""},
            {"field_id": 15630, "value": [mkb_item["name"]], "entity": [mkb_item["id"]], "comments": ""},

            # Общая информация
            {"field_id": 15619, "value": [gender_item["name"]], "entity": [gender_item["id"]], "comments": ""},
            {"field_id": 15649, "value": [decreted_item["name"]], "entity": [decreted_item["id"]], "comments": ""},
            {"field_id": 15648, "value": [yes_no_item["name"]], "entity": [yes_no_item["id"]], "comments": ""},
            {"field_id": 15669, "value": [previous_illness_item["name"]], "entity": [previous_illness_item["id"]],
             "comments": ""},
            {"field_id": 15696, "value": [yes_no_item["name"]], "entity": [yes_no_item["id"]], "comments": ""},
            {"field_id": 15686, "value": [observation_item["name"]], "entity": [observation_item["id"]],
             "comments": ""},
            {"field_id": 15902, "value": str(random.randint(10000, 99999)), "entity": "", "comments": ""},

            # Тяжесть и форма
            {"field_id": 15664, "value": [severity_item["name"]], "entity": [severity_item["id"]], "comments": ""},
            {"field_id": 15677, "value": [clinical_item["name"]], "entity": [clinical_item["id"]], "comments": ""},
            {"field_id": 15665, "value": [atypical_item["name"]], "entity": [atypical_item["id"]], "comments": ""},

            # Специфическая профилактика
            {"field_id": 15640, "value": [yes_no_item["name"]], "entity": [yes_no_item["id"]], "comments": ""},
            {"field_id": 15641, "value": random_date if yes_no_item["id"] == "282" else "", "entity": "",
             "comments": ""},
            {"field_id": 30385, "value": random_date if yes_no_item["id"] == "282" else "", "entity": "",
             "comments": ""},
            {"field_id": 15643, "value": [yes_no_item["name"]], "entity": [yes_no_item["id"]], "comments": ""},
            {"field_id": 15644, "value": random_date if yes_no_item["id"] == "282" else "", "entity": "",
             "comments": ""},
            {"field_id": 15668, "value": [emergency_item["name"]], "entity": [emergency_item["id"]], "comments": ""},

            # Дополнительно
            {"field_id": 16513, "value": f"Тестовая запись {random.randint(1, 999)}", "entity": "", "comments": ""},
            {"field_id": 20163, "value": random_bool, "entity": "", "comments": ""},
            {"field_id": 20844, "value": random_bool, "entity": "", "comments": ""},
            {"field_id": 30082, "value": random_bool, "entity": "", "comments": ""},
            {"field_id": 30083, "value": random_bool, "entity": "", "comments": ""},

            # Путешествия
            {"field_id": 30387, "value": [yes_no_item["name"]], "entity": [yes_no_item["id"]], "comments": ""},
            {"field_id": 30388, "value": [yes_no_item["name"]], "entity": [yes_no_item["id"]], "comments": ""},
            {"field_id": 30392, "value": [], "entity": [], "comments": ""},
            {"field_id": 30395, "value": [yes_no_item["name"]], "entity": [yes_no_item["id"]], "comments": ""},
            {"field_id": 30394, "value": [yes_no_item["name"]], "entity": [yes_no_item["id"]], "comments": ""},
            {"field_id": 30974, "value": [travel_item["name"]], "entity": [travel_item["id"]], "comments": ""},

            # Окончательный диагноз
            {"field_id": 15629, "value": today, "entity": "", "comments": ""},
            {"field_id": 15666, "value": [yes_no_item["name"]], "entity": [yes_no_item["id"]], "comments": ""},
            {"field_id": 30089, "value": [yes_no_item["name"]], "entity": [yes_no_item["id"]], "comments": ""},
            {"field_id": 19748, "value": [], "entity": [], "comments": ""},
            {"field_id": 30375, "value": [yes_no_item["name"]], "entity": [yes_no_item["id"]], "comments": ""},
            {"field_id": 30376, "value": random_date if yes_no_item["id"] == "282" else "", "entity": "",
             "comments": ""},

            # Возбудители
            {"field_id": 18906, "value": [yes_no_item["name"]], "entity": [yes_no_item["id"]], "comments": ""},
            {"field_id": 18907, "value": [yes_no_item["name"]], "entity": [yes_no_item["id"]], "comments": ""},
            {"field_id": 18908, "value": [], "entity": [], "comments": ""},
            {"field_id": 18910, "value": [], "entity": [], "comments": ""},
            {"field_id": 30097, "value": [yes_no_item["name"]], "entity": [yes_no_item["id"]], "comments": ""},
            {"field_id": 30098, "value": [yes_no_item["name"]], "entity": [yes_no_item["id"]], "comments": ""},
            {"field_id": 30099, "value": [], "entity": [], "comments": ""},
            {"field_id": 30100, "value": [], "entity": [], "comments": ""},
            {"field_id": 30101, "value": [], "entity": [], "comments": ""},
            {"field_id": 30102, "value": [], "entity": [], "comments": ""},
            {"field_id": 30401, "value": random_bool, "entity": "", "comments": ""},

            # Лечение
            {"field_id": 30103, "value": [yes_no_item["name"]], "entity": [yes_no_item["id"]], "comments": ""},
            {"field_id": 30105, "value": [], "entity": [], "comments": ""},
            {"field_id": 30366, "value": random_date if yes_no_item["id"] == "282" else "", "entity": "",
             "comments": ""},
            {"field_id": 30363, "value": [], "entity": [], "comments": ""},
            {"field_id": 30362, "value": "", "entity": "", "comments": ""},
            {"field_id": 30107, "value": [], "entity": [], "comments": ""},
            {"field_id": 30364, "value": "", "entity": "", "comments": ""},
            {"field_id": 30108, "value": [], "entity": [], "comments": ""},
            {"field_id": 30414, "value": "", "entity": "", "comments": ""},
            {"field_id": 30109, "value": [], "entity": [], "comments": ""},
            {"field_id": 30415, "value": "", "entity": "", "comments": ""},
            {"field_id": 30110, "value": [], "entity": [], "comments": ""},
            {"field_id": 30416, "value": "", "entity": "", "comments": ""},

            # Исход
            {"field_id": 15658, "value": [outcome_item["name"]], "entity": [outcome_item["id"]], "comments": ""},
            {"field_id": 15662, "value": today, "entity": "", "comments": ""},
            {"field_id": 15661, "value": [], "entity": [], "comments": ""},
            {"field_id": 30384, "value": [], "entity": [], "comments": ""},
            {"field_id": 30378, "value": [yes_no_item["name"]], "entity": [yes_no_item["id"]], "comments": ""},
            {"field_id": 30379, "value": [], "entity": [], "comments": ""},
            {"field_id": 30380, "value": [], "entity": [], "comments": ""},
            {"field_id": 30381, "value": [], "entity": [], "comments": ""},
            {"field_id": 30382, "value": [], "entity": [], "comments": ""},
            {"field_id": 30383, "value": [], "entity": [], "comments": ""},

            # Трансфузии
            {"field_id": 30377, "value": [yes_no_item["name"]], "entity": [yes_no_item["id"]], "comments": ""},
            {"field_id": 30404, "value": [yes_no_item["name"]], "entity": [yes_no_item["id"]], "comments": ""},
            {"field_id": 30405, "value": random_date if yes_no_item["id"] == "282" else "", "entity": "",
             "comments": ""},
            {"field_id": 30406, "value": [], "entity": [], "comments": ""},
        ]
    }