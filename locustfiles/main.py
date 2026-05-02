from locust import HttpUser, between, events, task, tag

from accounts.loader import load_users
from accounts.pool import AccountPool
from clients.auth_client import AuthClient
from scenarios.user_flows import visit_random_form, visit_random_arm


@events.init.add_listener
def on_locust_init(environment, **_kwargs) -> None:
    accounts = load_users()
    environment.account_pool = AccountPool(accounts)


class ApiUser(HttpUser):
    wait_time = between(1, 3)

    def on_start(self) -> None:
        # Инициализируем атрибуты заранее, чтобы task не падали,
        # если login не удался.
        self.account = None
        self.access_token = None
        self.auth_client = AuthClient(self.client)

        # Берем аккаунт из общего пула.
        self.account = self.environment.account_pool.acquire()
        self.username = self.account.username
        self.password = self.account.password
        self.rid = self.account.rid

        # Логинимся один раз при старте виртуального пользователя.
        response = self.auth_client.login(self.username, self.password)
        if response.status_code != 200:
            print(
                f"Ошибка при входе для пользователя "
                f"{self.username}: {response.status_code}"
            )
            return

        data = response.json()
        self.access_token = data.get("access_token")

        if not self.access_token:
            print(f"Не получили access_token для {self.username}")
            return

        print(f"Пользователь {self.username} успешно вошел в систему")

    def on_stop(self) -> None:
        if self.access_token:
            logout_response = self.auth_client.logout(self.access_token)
            print(
                f"Пользователь {self.username}: "
                f"logout status {logout_response.status_code}"
            )

        if self.account is not None:
            self.environment.account_pool.release(self.account)
    @tag("form")
    @task
    def open_form(self) -> None:
        if not self.access_token:
            return

        visit_random_form(self)

    @tag("arm")
    @task
    def visit_random_arm(self) -> None:
        if not self.access_token:
            return
        visit_random_arm(self)


