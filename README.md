# FormLoadTests

Нагрузочные тесты на `Locust` для HTTP API с разделением на отдельные профили:

- `happy` - валидная бизнес-нагрузка;
- `medium` - средняя смешанная нагрузка на чтение, create и patch;
- `ramp` - ступенчатое наращивание пользователей до деградации сервиса;
- `negative` - невалидные payload'ы и проверка reject-path;
- `stress` - более агрессивная валидная нагрузка на тех же сценариях.

## Стек

- Python 3.10+ (`venv` в проекте создан на Python 3.14)
- `locust`
- `pydantic`
- `keyring`

## Структура проекта

```text
accounts/
  loader.py              # загрузка аккаунтов из secrets + keyring
  models.py              # pydantic-модели аккаунтов
  pool.py                # потокобезопасный пул аккаунтов
api/
  auth.py                # login/logout
  forms.py               # open form / open arm / create form
payloads/
  form_116/
    dictionaries.py      # справочники и random value helpers
    valid.py             # валидные payload builder'ы
    invalid.py           # невалидные payload builder'ы
scenarios/
  happy/
    forms.py             # открытие анкет и ARM
    create_form_116.py   # создание валидной формы 116
  negative/
    create_form_116.py   # отправка невалидной формы 116
locustfiles/
  base.py                # общий BaseApiUser и init account pool
  happy.py               # основной happy-path suite
  medium.py              # профиль средней смешанной нагрузки
  ramp_until_degradation.py  # ступенчатый рост пользователей до деградации
  negative.py            # suite для validation/reject-path
  stress.py              # suite для усиленной валидной нагрузки
  main.py                # совместимость со старым happy entrypoint
scripts/
  seed_keyring.py        # массовая запись общего пароля в keyring
  read_users.py          # вспомогательная загрузка аккаунтов в dict-виде
```

## Подготовка

### 1. Установить зависимости

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Подготовить список тестовых пользователей

Проект ожидает файл `secrets/test_users.json` со структурой:

```json
[
  {
    "alias": "u001",
    "username": "user1@example.com",
    "rid": "267"
  },
  {
    "alias": "u002",
    "username": "user2@example.com",
    "rid": "195"
  }
]
```

Поля:

- `alias` - ключ для поиска пароля в `keyring`;
- `username` - логин пользователя;
- `rid` - дополнительный идентификатор аккаунта, который хранится в runtime-модели.

Каталог `secrets/` добавлен в `.gitignore`, поэтому хранить в нем локальные тестовые данные допустимо.

### 3. Записать пароли в `keyring`

Пароли не читаются из JSON-файла. Для каждого `alias` проект берет пароль из системного `keyring` с сервисом `form-load-tests`.

Если у всех тестовых пользователей один и тот же пароль:

```bash
python3 scripts/seed_keyring.py
```

Скрипт запросит пароль и сохранит его для алиасов `u001`-`u010`.

Важно:

- алиасы в `keyring` должны совпадать с `alias` в `secrets/test_users.json`;
- если пароль для алиаса не найден, запуск завершится ошибкой;
- если аккаунтов меньше, чем одновременно стартующих пользователей `Locust`, часть пользователей упадет на получении аккаунта из пула.

## Запуск

Хост приложения не зашит в код и передается через параметр `--host`.

### Happy-path suite

```bash
locust -f locustfiles/happy.py --host https://example.test
```

Headless:

```bash
locust -f locustfiles/happy.py \
  --host https://example.test \
  --headless \
  --users 8 \
  --spawn-rate 2 \
  --run-time 5m
```

### Negative suite

Отправляет намеренно некорректные payload'ы формы `116` и ожидает reject-path (`400/422`).

```bash
locust -f locustfiles/negative.py --host https://example.test
```

### Stress suite

Использует валидные happy-сценарии, но с более плотным темпом запросов.

```bash
locust -f locustfiles/stress.py --host https://example.test
```

### Совместимость со старым entrypoint

Старый запуск оставлен как алиас happy-suite:

```bash
locust -f locustfiles/main.py --host https://example.test
```

## Готовые сценарии на 9 пользователей

Ниже три минимальных сценария, которые соответствуют текущей реализации проекта и не требуют ручного подбора тегов.

### 1. Базовый happy-path

Что проверяет:

- login/logout;
- открытие случайных анкет;
- переходы в ARM;
- смешанные валидные create-операции по формам `116`, `119`, `183`.

Запуск:

```bash
./.venv/bin/locust --config config/happy.stage.conf
```

### 2. Чистая нагрузка на создание анкет

Что проверяет:

- только операции записи;
- создание форм `116`, `119`, `183` без открытия форм и без soft-delete;
- базовую insert-нагрузку на backend и БД.

Запуск:

```bash
./.venv/bin/locust --config config/create.stage.conf
```

### 3. Жизненный цикл формы 119: create + patch

Что проверяет:

- создание анкеты формы `119`;
- soft-delete через `PATCH` (`is_active = false`);
- отдельную update-нагрузку на backend и БД.

Запуск:

```bash
./.venv/bin/locust --config config/patch.stage.conf
```

### 4. Средняя смешанная нагрузка

Что проверяет:

- открытие случайных анкет;
- переходы в ARM;
- создание форм `116`, `119`, `183`;
- soft-delete формы `119` через `PATCH`;
- более плотный темп без перехода в тяжёлый stress-профиль.

Вес задач в профиле `medium`:

- `open_form` - `4`
- `visit_random_arm` - `8`
- `116-create` - `4`
- `119-create` - `4`
- `183-create` - `4`
- `119-patch` - `3`

Отдельно:

- `spawn-rate = 2`
- `users = 9`
- `run-time = 7m`
- `wait_time = 0.5..1.5s`

Запуск:

```bash
./.venv/bin/locust --config config/medium.stage.conf
```

Примечание по ARM:

- в текущей реализации переходы в ARM выполняет только пользователь с алиасом `u001`, поэтому вес `visit_random_arm` повышен, чтобы ARM-активность не потерялась на фоне остальных задач.

### 5. Ступенчатый рост пользователей до деградации

Что проверяет:

- стартует с `10` пользователей;
- каждые `5` минут добавляет ещё `5` пользователей;
- использует workload профиля `medium`;
- останавливается автоматически, когда сервис стабильно деградирует.

Правила автостопа:

- `p95 >= 3000 ms` по общей статистике;
- или `fail_ratio >= 10%`;
- и нарушение держится `15` проверок подряд после warmup.

Дополнительно:

- `spawn-rate = 1`
- `warmup = 2m`
- `min_requests_before_stop = 200`
- верхняя граница пользователей берётся автоматически из `secrets/test_users.json`

Запуск:

```bash
./.venv/bin/locust --config config/ramp.stage.conf
```

## Что делает каждый профиль

### `happy`

1. На этапе `events.init` загружается список аккаунтов и создается общий `AccountPool`.
2. Виртуальный пользователь получает свободный аккаунт и логинится один раз.
3. Выполняет валидные действия: открытие случайной анкеты, переход в ARM, создание форм `116`, `119`, `183`.
4. При остановке выполняет logout и возвращает аккаунт обратно в пул.

### `negative`

1. Использует тот же login/logout и пул аккаунтов.
2. Генерирует невалидные payload'ы формы `116`.
3. Проверяет, что сервис отклоняет их контролируемо, без `5xx`.

### `stress`

1. Использует те же валидные сценарии, что и `happy`.
2. Уменьшает паузы между запросами и повышает долю create-операций.
3. Для формы `119` дополнительно может выполнять сценарий `create + patch`.

### `medium`

1. Использует все основные happy-path действия.
2. Увеличивает долю create/update-операций относительно базового `happy`.
3. Ускоряет разогрев (`spawn-rate = 2`) и уменьшает паузы между действиями.

### `ramp`

1. Использует те же действия, что и `medium`.
2. Начинает с `10` пользователей и добавляет по `5` каждые `5` минут.
3. Автоматически завершает тест при устойчивой деградации по задержкам или ошибкам.

## Текущее состояние

- В negative-профиле пока реализован один тип негативного направления: невалидная отправка формы `116`.
- Stress-профиль сейчас строится на тех же бизнес-сценариях, что и happy, но с более агрессивным pacing.
- Если появятся новые формы, их лучше добавлять как отдельные подпакеты в `payloads/`, а не складывать в общий `data/`.
