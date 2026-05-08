from locust import between, tag, task

from locustfiles.base import BaseApiUser
from scenarios.happy.create_form_116 import create_form_116
from scenarios.happy.forms import open_random_form


class StressUser(BaseApiUser):
    wait_time = between(0.1, 0.5)

    @tag("stress", "form")
    @task(2)
    def open_form(self) -> None:
        if not self.access_token:
            return

        open_random_form(self)

    @tag("stress", "116-create")
    @task(8)
    def new_anket_116(self) -> None:
        if not self.access_token:
            return

        create_form_116(self)
