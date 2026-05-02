import json
from pathlib import Path

import keyring

SERVICE_NAME = "form-load-tests"
PROJECT_ROOT = Path(__file__).resolve().parent.parent
USERS_PATH = PROJECT_ROOT / "secrets" / "test_users.json"


def load_users() -> list[dict[str, str]]:
    users = json.loads(USERS_PATH.read_text(encoding="utf-8"))

    for user in users:
        password = keyring.get_password(SERVICE_NAME, user["alias"])
        user["password"] = password

    return users

