from accounts.loader import load_users as load_runtime_users


def load_users() -> list[dict[str, str]]:
    return [account.model_dump() for account in load_runtime_users()]
