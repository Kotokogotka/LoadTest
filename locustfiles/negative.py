from locust import tag, task

from locustfiles.base import BaseApiUser
from scenarios.negative.create_form_116 import create_invalid_form_116


class NegativeValidationUser(BaseApiUser):
    @tag("negative", "116-invalid")
    @task
    def create_invalid_anket_116(self) -> None:
        if not self.access_token:
            return

        create_invalid_form_116(self)
