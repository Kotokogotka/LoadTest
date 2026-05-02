import json
from pathlib import Path

import keyring

from accounts.models import RuntimeAccount, StoredAccount

DEFAULT_SERVICE_NAME = "form-load-tests"
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_USERS_PATH = PROJECT_ROOT / "secrets" / "test_users.json"


def _read_stored_accounts(users_path: Path) -> list[StoredAccount]:
    raw_users = json.loads(users_path.read_text(encoding="utf-8"))
    return [StoredAccount.model_validate(item) for item in raw_users]


def _get_password(service_name: str, alias: str) -> str:
    password = keyring.get_password(service_name, alias)
    if not password:
        raise ValueError(
            f"Password for alias={alias!r} was not found in keyring "
            f"for service={service_name!r}"
        )
    return password


def load_users(
    users_path: Path | None = None,
    service_name: str = DEFAULT_SERVICE_NAME,
) -> list[RuntimeAccount]:
    target_path = users_path or DEFAULT_USERS_PATH
    stored_accounts = _read_stored_accounts(target_path)

    return [
        RuntimeAccount(
            alias=account.alias,
            username=account.username,
            password=_get_password(service_name, account.alias),
            rid=account.rid,
        )
        for account in stored_accounts
    ]

