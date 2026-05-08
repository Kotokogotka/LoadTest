import random

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


def get_random_mkb():
    item = random.choice(MKB_ITEMS)
    return {"id": item["id"], "name": item["name"]}


GENDER = [
    {"id": "1", "name": "Мужской"},
    {"id": "2", "name": "Женский"},
]


def get_random_gender():
    item = random.choice(GENDER)
    return {"id": item["id"], "name": item["name"]}


YES_NO = [
    {"id": "282", "name": "Да"},
    {"id": "283", "name": "Нет"},
]


def get_random_yes_no():
    item = random.choice(YES_NO)
    return {"id": item["id"], "name": item["name"]}


DECRETED_WORKERS = [
    {"id": "76949", "name": "Медицинский работник"},
    {"id": "76951", "name": "Нет"},
    {"id": "78817", "name": "Работник аптек, других фармацевтических учреждений"},
    {"id": "78820", "name": "Работник бассейнов, водолечебниц"},
    {"id": "78814", "name": "Работник водопроводных и канализационных сооружений"},
    {"id": "78812", "name": "Работник детских дошкольных учреждений"},
    {"id": "78811", "name": "Работник животноводческих комплексов, молочно-товарных ферм"},
    {"id": "76948", "name": "Работник коммунально-бытового обслуживания населения"},
    {"id": "78815", "name": "Работник ЛПУ, санаториев, домов отдыха, пансионатов, домов инвалидов и престарелых"},
    {"id": "78816", "name": "Работник мест временного проживания (общежития, гостиницы, хостелы и т.п.)"},
    {"id": "78813", "name": "Работник оздоровительных учреждений"},
    {"id": "78819", "name": "Работник, работающие вахтовым методом"},
    {"id": "76947", "name": "Работник, связанный с продуктами питания"},
    {"id": "78818", "name": "Работник социальной сферы"},
    {"id": "76963", "name": "Работник транспорта"},
    {"id": "76950", "name": "Работник учебно-воспитательных учреждений"},
]


def get_random_decreted_worker():
    item = random.choice(DECRETED_WORKERS)
    return {"id": item["id"], "name": item["name"]}


PREVIOUS_ILLNESS = [
    {"id": "77437", "name": "Более 2-х лет назад"},
    {"id": "77436", "name": "Более года назад"},
    {"id": "76990", "name": "Год назад"},
    {"id": "76988", "name": "Две недели назад"},
    {"id": "76973", "name": "Месяц назад"},
    {"id": "76972", "name": "Нет"},
    {"id": "76974", "name": "Пол года назад"},
    {"id": "76989", "name": "Три месяца назад"},
]


def get_random_previous_illness():
    item = random.choice(PREVIOUS_ILLNESS)
    return {"id": item["id"], "name": item["name"]}


OBSERVATION_TYPES = [
    {"id": "71988", "name": "Амбулаторно"},
    {"id": "100004", "name": "Диспансеризация (скрининг)"},
    {"id": "100005", "name": "Санаторно-курортное лечение"},
    {"id": "71989", "name": "Стационар"},
    {"id": "74215", "name": "стационар и амб. долечивание"},
]


def get_random_observation_type():
    item = random.choice(OBSERVATION_TYPES)
    return {"id": item["id"], "name": item["name"]}


EMERGENCY_PREVENTION_TYPES = [
    {"id": "76987", "name": "Анатоксины"},
    {"id": "76964", "name": "Антибиотикопрофилактика"},
    {"id": "78057", "name": "Антирабическая вакцина"},
    {"id": "85937", "name": "Антитоксин ботулинический типа A"},
    {"id": "85938", "name": "Антитоксин ботулинический типа B"},
    {"id": "76986", "name": "Иммуномодуляторы"},
    {"id": "76967", "name": "Иммунопрофилактика. Иммуноглобулины"},
    {"id": "76966", "name": "Иммунопрофилактика. Сыворотки"},
    {"id": "76965", "name": "Фагопрофилактика"},
    {"id": "76985", "name": "Эубиотики"},
]


def get_random_emergency_prevention():
    item = random.choice(EMERGENCY_PREVENTION_TYPES)
    return {"id": item["id"], "name": item["name"]}


SEVERITY_TYPES = [
    {"id": "71420", "name": "легкое"},
    {"id": "86061", "name": "нетяжелое (для пневмоний)"},
    {"id": "71421", "name": "среднее"},
    {"id": "71422", "name": "тяжелое"},
]


def get_random_severity():
    item = random.choice(SEVERITY_TYPES)
    return {"id": item["id"], "name": item["name"]}


CLINICAL_FORMS = [
    {"id": "76976", "name": "Атипичная"},
    {"id": "76975", "name": "Типичная"},
]


def get_random_clinical_form():
    item = random.choice(CLINICAL_FORMS)
    return {"id": item["id"], "name": item["name"]}


ATYPICAL_FORMS = [
    {"id": "78550", "name": "Абортивная"},
    {"id": "78549", "name": "Молниеносная"},
    {"id": "100003", "name": "Общий"},
    {"id": "78548", "name": "Стертая"},
]


def get_random_atypical_form():
    item = random.choice(ATYPICAL_FORMS)
    return {"id": item["id"], "name": item["name"]}


TRAVEL_STATUSES = [
    {"id": "100633", "name": "В путешествии не был"},
    {"id": "100631", "name": "За границей"},
    {"id": "100630", "name": "По России"},
    {"id": "100632", "name": "По России/за границей"},
]


def get_random_travel_status():
    item = random.choice(TRAVEL_STATUSES)
    return {"id": item["id"], "name": item["name"]}


OUTCOMES = [
    {"id": "86062", "name": "Выздоровел"},
    {"id": "76957", "name": "Летальный"},
    {"id": "76952", "name": "Переболел"},
]


def get_random_outcome():
    item = random.choice(OUTCOMES)
    return {"id": item["id"], "name": item["name"]}
