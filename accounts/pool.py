from collections import deque
from threading import Lock

from accounts.models import RuntimeAccount


class AccountPool:
    def __init__(self, accounts: list[RuntimeAccount]) -> None:
        # Проверка на наличие хотя бы одного аккаунта в пуле
        if not accounts:
            raise ValueError("Pool аккаунтов пустой")
        # Тут хранятся свободные аккаунты
        self._free_accounts = deque(accounts)

        # Тут храняться аккаунты которые находятся в работе
        self._in_use_aliases: set[str] = set()

        # Lock будет использоваться для одновременного
        # доступа нескольких пользователей к одному аккаунту
        self._lock = Lock()

    def acquire(self) -> RuntimeAccount:
        # Берем lock, чтобы 2 потока не получили одновременно один аккаунт
        with self._lock:
            # Если свободных аккаунтов нет, то выдаем ошибку
            if not self._free_accounts:
                raise RuntimeError('Нет ни одного аккаунта в пуле')

            # Забираем первый свободный аккаунт из очереди
            account = self._free_accounts.popleft()

            # Переводим в состоние занятого аккаунта
            self._in_use_aliases.add(account.alias)

            return account

    def release(self, account: RuntimeAccount) -> None:
        # Возвращаем аккаунт обратно в pool при помощи lock
        with self._lock:
            # Обработки ошибки если статус аккаута не правильно определен
            if account.alias not in self._in_use_aliases:
                raise ValueError(
                    f"ERROR: Аккаунт {account.alias} не числится в списке используемых"
                )

            # Убираем аккаунт из списка используемых
            self._in_use_aliases.remove(account.alias)

            # Добавляем аккаунт в список не используемых
            self._free_accounts.append(account)

    # Возвращает кол-во свободных аккаунтов
    def available(self) -> int:
        with self._lock:
            return len(self._free_accounts)

    def in_use_count(self) -> int:
        with self._lock:
            return len(self._in_use_aliases)


