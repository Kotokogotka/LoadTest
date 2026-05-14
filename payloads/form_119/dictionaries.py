import random


# Возвращает рандомные даты для полей с датами 15803, 20544, 15878
def field_date_15803_20544_15878():
    field = (
            f"{random.randint(2023, 2026)}-"
            f"{random.randint(1, 12):02d}-"
            f"{random.randint(1, 28):02d}"
        )
    return field

# Список случайных адресов для поля 30973
ADDRESS = ["Москва, пер.Красный, дом 1234, этаж 12, кв.1900",
           "Lytkarino, kvartal 2, dom 5, kv. 37",
           "Россия, Самарская область, г.Сызрань,"
           " ул. 5-ая конечная, дом 67/9, 2 подъезд, третья лавочка от ларька."]

# Возвращает адрес для поля 30973
def fields_30973():
    items = random.choice(ADDRESS)
    return items


# Список МКБ для поля 15804
MKB_ITEMS = [
    {"id": "265", "name": "A50 - Врожденный сифилис"},
    {"id": "275", "name": "A51 - Ранний сифилис"},
    {"id": "283", "name": "A52 - Поздний сифилис"},
    {"id": "293", "name": "A53.9 - Сифилис неуточненный"},
    {"id": "524", "name": "B16 - Острый гепатит B"},
    {"id": "531", "name": "B17.1 - Острый гепатит C"},
    {"id": "537", "name": "B18.2 - Хронический вирусный гепатит C"},
    {"id": "544", "name": "B20 - ВИЧ-инфекция"},
    {"id": "4306", "name": "J18.0 - Бронхопневмония неуточненная"},
    {"id": "4286", "name": "J15.0 - Пневмония, вызванная Klebsiella pneumoniae"},
    {"id": "551", "name": "B20.6 - Пневмония, вызванная Pneumocystis carinii"},
    {"id": "4293", "name": "J12.2 - Пневмония, вызванная метапневмовирусом"},
    {"id": "4303", "name": "J17.2 - Пневмония при гриппе"},
    {"id": "564", "name": "B22.0 - ВИЧ-энцефалопатия"},
    {"id": "570", "name": "B23.1 - ВИЧ с генерализованной лимфаденопатией"},
]

# Случайные значения МКБ для поля 15804
def fields_15804():
    items = random.choice(MKB_ITEMS)
    return {"id": items["id"], "name": items["name"]}


def fields_16434():
    items = random.choice(MKB_ITEMS)
    return {"id": items["id"], "name": items["name"]}


CITY = [
    {"id": 207, "name": "Асбест"},
    {"id": 218, "name": "Бавлы"},
    {"id": 219, "name": "Баксан"},
    {"id": 304, "name": "Буча"},
    {"id": 307, "name": "Быково"},
    {"id": 1699, "name": "Голубое"},
    {"id": 1697, "name": "Яренск"},
    {"id": 1709, "name": "Шимск"},
    {"id": 1771, "name": "Велиж"},
    {"id": 71, "name": "Kaunas"},
    {"id": 72, "name": "Kingston"},
    {"id": 90, "name": "Mainz"},
    {"id": 80, "name": "Lisboa"},
    {"id": 98, "name": "Milano"},
    {"id": 65, "name": "Hong Kong"},
    {"id": 82, "name": "Liverpool"},
]

def fields_16567():
    items = random.choice(CITY)
    return {"id": items["id"], "name": items["name"]}


LOCALIZATION = [
    {"id": 78364, "name": "Дошкольные учреждения"},
    {"id": 77356, "name": "Жилая зона"},
    {"id": 78594, "name": "Лесопарковая зона"},
    {"id": 77463, "name": "Летние оздоровительные учреждения (дети)"},
    {"id": 77350, "name": "Медицинские организации"},
    {"id": 77464, "name": "Образовательные организации (дети)"},
    {"id": 77352, "name": "Организации, обслуживаемые ФМБА России"},
    {"id": 77470, "name": "Организованный коллектив (взрослые)"},
    {"id": 78593, "name": "Природный объект"},
    {"id": 77351, "name": "Социальные объекты (взрослые)"},
    {"id": 78366, "name": "Учреждения для детей-сирот"},
    {"id": 78365, "name": "Учреждения для детей с отклонением развития"},
    {"id": 78367, "name": "Учреждения дополнительного образования (дети)"},
    {"id": 78363, "name": "Учреждения отдыха и оздоровления (взрослые)"},
    {"id": 77462, "name": "Учреждения санитарно-курортного лечения (взрослые)"}
]

def fields_15859():
    items = random.choice(LOCALIZATION)
    return {"id": items["id"], "name": items["name"]}


TRANSMISSION_PATHS = [
    {"id": 100572, "name": "ассоциированный с инвазивными процедурами"},
    {"id": 100571, "name": "ассоциированный с операциями"},
    {"id": 100561, "name": "водный"},
    {"id": 100563, "name": "воздушно-капельный"},
    {"id": 100564, "name": "воздушно-пылевой"},
    {"id": 100575, "name": "восходящий "},
    {"id": 100574, "name": "герминативный/гемо-трансплацентарный (антенатальный)"},
    {"id": 100568, "name": "инокуляционный"},
    {"id": 100576, "name": "(интранатальный) во время родов "},
    {"id": 100569, "name": "инъекционный"},
    {"id": 100562, "name": "контактно-бытовой"},
    {"id": 100567, "name": "контаминационный"},
    {"id": 100566, "name": "непрямой"},
    {"id": 100578, "name": "не установлен"},
    {"id": 100560, "name": "пищевой (алиментарный)"},
    {"id": 100565, "name": "прямой"},
    {"id": 100573, "name": "трансплантанционный"},
    {"id": 100570, "name": "трансфузионный"},
    {"id": 100577, "name": "уточняется"}
]

def fields_15916():
    items = random.choice(TRANSMISSION_PATHS)
    return {"id": items["id"], "name": items["name"]}


YES_NO = [
    {"id": 282, "name": "Да"},
    {"id": 283, "name": "Нет"}
]

def fields_15917():
    items = random.choice(YES_NO)
    return {"id": items["id"], "name": items["name"]}

def fields_20258():
    items = random.choice(YES_NO)
    return {"id": items["id"], "name": items["name"]}

# Поле примечание
NOTE = ["Тут должен быть текст для примечания, чтобы было что-то полезное",
        "Nen ljk;ty ,snm ntrcn +& (&&&**%&$#$^&!)@(!#*) это для теста"]

def fields_16433():
    items = random.choice(NOTE)
    return items


VALID_CNT = ["1", "33", "1112", "44", "9", "54", "9", "0", "23", "14"]
INVALID_CNT = ["1o", "&^%&())@", "!@#", "SixSeven", "Nine", "five", "09", "o"]
def fields_15860():
    items = random.choice(VALID_CNT)
    return items

VALID_20367 = ["1", "33", "1112", "44", "9", "54", "9", "0", "23", "14"]

def fields_20367():
    items = random.choice(VALID_CNT)
    return items

def fields_20368():
    items = random.choice(VALID_CNT)
    return items

def fields_20369():
    items = random.choice(VALID_CNT)
    return items

def fields_20370():
    items = random.choice(VALID_CNT)
    return items

def fields_15862():
    items = random.choice(VALID_CNT)
    return items

def fields_15861():
    items = random.choice(VALID_CNT)
    return items

def fields_15863():
    items = random.choice(VALID_CNT)
    return items

def fields_20371():
    items = random.choice(VALID_CNT)
    return items

def fields_20372():
    items = random.choice(VALID_CNT)
    return items

def fields_20373():
    items = random.choice(VALID_CNT)
    return items

def fields_20374():
    items = random.choice(VALID_CNT)
    return items

def fields_15865():
    items = random.choice(VALID_CNT)
    return items

def fields_15864():
    items = random.choice(VALID_CNT)
    return items

def fields_15870():
    items = random.choice(VALID_CNT)
    return items

def fields_15869():
    items = random.choice(VALID_CNT)
    return items

def fields_15868():
    items = random.choice(VALID_CNT)
    return items

def fields_15867():
    items = random.choice(VALID_CNT)
    return items































