from locust import between, tag, task

from locustfiles.base import BaseApiUser
from scenarios.happy.create_form_116 import create_form_116
from scenarios.happy.create_form_119 import create_and_soft_delete_form_119, create_form_119
from scenarios.happy.create_form_183 import create_form_183
from scenarios.happy.forms import open_random_arm, open_random_form


class MediumLoadUser(BaseApiUser):
    wait_time = between(0.5, 1.5)

    @tag("medium", "form")
    @task(4)
    def open_form(self) -> None:
        if not self.access_token:
            return

        open_random_form(self)

    @tag("medium", "arm")
    @task(8)
    def visit_random_arm(self) -> None:
        if not self.access_token:
            return

        open_random_arm(self)

    @tag("medium", "116-create", "116 create", "116", "create")
    @task(4)
    def new_anket_116(self) -> None:
        if not self.access_token:
            return

        create_form_116(self)

    @tag("medium", "119-create", "119 create", "119", "create")
    @task(4)
    def new_anket_119(self) -> None:
        if not self.access_token:
            return

        create_form_119(self)

    @tag("medium", "183-create", "183 create", "183", "create")
    @task(4)
    def new_anket_183(self) -> None:
        if not self.access_token:
            return

        create_form_183(self)

    @tag("medium", "119-patch", "119 patch", "119", "patch", "soft-delete")
    @task(3)
    def patch_anket_119(self) -> None:
        if not self.access_token:
            return

        create_and_soft_delete_form_119(self)
