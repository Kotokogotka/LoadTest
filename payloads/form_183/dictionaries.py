import random


RESEARCH_COMPLETED = [
    {"id": 78027, "name": "в лаборатории не ФМБА"},
    {
        "id": 78026, "name": "в собственной лаборатории"}
]

def get_random_research_completed():
    item = random.choice(RESEARCH_COMPLETED)
    return {"id": item["id"], "name": item["name"]}


RESEARCH_CLIENT = [
    {"id": 78031, "name": "для себя"},
    {"id": 78029, "name": "другая МО (не ФМБА)"},
    {"id": 78028, "name": "МО ФМБА"},
    {"id": 78569, "name": "По предписанию МРУ (ТО)"},
    {"id": 78030, "name": "частное лицо"},
]

def get_random_reserch_client():
    item = random.choice(RESEARCH_CLIENT)
    return {"id": item["id"], "name": item["name"]}


TAXONOMIC_ITEMS = [
    {"id": 48, "name": "Alternaria tenuissima"},
    {"id": 49, "name": "Anaplasma phagocytophilum"},
    {"id": 50, "name": "Ancylostoma duodenale"},
    {"id": 51, "name": "Anisakis physeteris"},
    {"id": 52, "name": "Anisakis simplex"},
    {"id": 53, "name": "Anisakis spp."},
    {"id": 54, "name": "Aphanoascus fulvescens (анаморфа - Chrysosporium)"},
    {"id": 55, "name": "Apophysomyces elegans"},
    {"id": 56, "name": "Ascaris lumbricoides"},
    {"id": 57, "name": "Askaris suum"},
    {"id": 110, "name": "Bacteroides propionicifaciens"},
    {"id": 111, "name": "Bacteroides pyogenes"},
    {"id": 112, "name": "Bacteroides reticulotermitis"},
    {"id": 113, "name": "Bacteroides rodentium"},
    {"id": 114, "name": "Bacteroides salanitronis"},
    {"id": 115, "name": "Bacteroides salyersiae"},
    {"id": 116, "name": "Bacteroides sartorii"},
    {"id": 117, "name": "Bacteroides spp."},
    {"id": 118, "name": "Bacteroides stercorirosoris"},
    {"id": 119, "name": "Bacteroides stercoris"},
    {"id": 120, "name": "Bacteroides thetaiotaomicron"},
    {"id": 121, "name": "Bacteroides timonensis"},
    {"id": 122, "name": "Bacteroides uniformis"},
    {"id": 123, "name": "Bacteroides vulgatus"},
    {"id": 124, "name": "Bacteroides xylanisolvens"},
    {"id": 125, "name": "Bacteroides xylanolyticus"},
    {"id": 126, "name": "Bacteroides zoogleoformans"},
    {"id": 127, "name": "Balantidium coli"},
    {"id": 128, "name": "Basidiobolus haptosporus"},
]

def get_random_taxonomic_items():
    items = random.choice(TAXONOMIC_ITEMS)
    return {"id": items["id"], "name": items["name"]}


SOURCE_OF_SELECTIONS = [
    {"id": 78379, "name": "Плазма крови "},
    {"id": 78386, "name": "Потожировые выделения "},
    {"id": 86939, "name": "Промывные воды"},
    {"id": 78454, "name": "Пунктат бубона"},
    {"id": 86965, "name": "Пунктат из пораженного органа"},
    {"id": 78453, "name": "Пунктат костного мозга"},
    {"id": 86966, "name": "Пунктат суставной жидкости из коленного сустава"},
    {"id": 78394, "name": "Рвотные массы"},
    {"id": 78387, "name": "Секрет предстательной железы "},
    {"id": 78388, "name": "Слюна "},
    {"id": 78426, "name": "Смыв из верхних дыхательных путей "},
    {"id": 78427, "name": "Смыв из мочевого пузыря "},
    {"id": 78428, "name": "Смыв из нижних дыхательных путей "},
    {"id": 78429, "name": "Смыв из ротоглотки "},
    {"id": 78430, "name": "Смыв первичного аффекта "},
    {"id": 78431, "name": "Смыв трахеобронхиальный "},
    {"id": 78450, "name": "Соскоб с роговицы "},
]

def get_random_source_of_selection():
    items = random.choice(SOURCE_OF_SELECTIONS)
    return {"id": items["id"], "name": items["name"]}


RESEARCH_METHOD = [
    {"id": 86234, "name": "ELISA-тест"},
]

def get_random_research_method():
    items = random.choice(RESEARCH_METHOD)
    return {"id": items["id"], "name": items["name"]}


EXTERNAL_LABS = [
    {"id": 94, "name": "БУЗОО «ЖК № 1»"},
    {"id": 95, "name": "БУЗОО «Городской клинический перинатальный центр»"},
    {"id": 96, "name": "БУЗОО РД № 2"},
    {"id": 97, "name": "БУЗОО «РД № 4»"},
    {"id": 98, "name": "БУЗОО «Клинический родильный дом № 6»"},
    {"id": 99, "name": "БУЗОО ГП № 3"},
    {"id": 100, "name": "БУЗОО ГП №4"},
]

def get_random_external_lab():
    items = random.choice(EXTERNAL_LABS)
    return {"id": items["id"], "name": items["name"]}
