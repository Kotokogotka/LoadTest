from locust import tag, task

from locustfiles.base import BaseApiUser
from scenarios.happy.create_form_116 import create_form_116
from scenarios.happy.forms import open_random_arm, open_random_form


class HappyPathUser(BaseApiUser):
    @tag("form", "happy")
    @task(2)
    def open_form(self) -> None:
        if not self.access_token:
            return

        open_random_form(self)

    @tag("arm", "happy")
    @task(1)
    def visit_random_arm(self) -> None:
        if not self.access_token:
            return

        open_random_arm(self)

    @tag("116-create", "happy")
    @task(5)
    def new_anket_116(self) -> None:
        if not self.access_token:
            return

        create_form_116(self)
