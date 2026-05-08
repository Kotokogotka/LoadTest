from locust import HttpUser, between, events

from accounts.loader import load_users
from accounts.pool import AccountPool
from api.auth import AuthClient
from api.forms import FormsClient


@events.init.add_listener
def on_locust_init(environment, **_kwargs) -> None:
    if getattr(environment, "account_pool", None) is None:
        environment.account_pool = AccountPool(load_users())


class BaseApiUser(HttpUser):
    abstract = True
    wait_time = between(1, 3)

    def on_start(self) -> None:
        self.account = None
        self.access_token = None
        self.username = None
        self.password = None
        self.rid = None
        self.auth_client = AuthClient(self.client)
        self.forms_client = FormsClient(self.client)

        self.account = self.environment.account_pool.acquire()
        self.username = self.account.username
        self.password = self.account.password
        self.rid = self.account.rid

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
