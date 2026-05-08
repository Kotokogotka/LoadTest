from payloads.form_116.invalid import build_random_invalid_form_116_payload

EXPECTED_REJECTION_STATUSES = {400, 422}


def create_invalid_form_116(user) -> None:
    payload = build_random_invalid_form_116_payload()
    response = user.forms_client.create_form(payload, user.access_token)

    if response.status_code in EXPECTED_REJECTION_STATUSES:
        print(
            f"Некорректный payload формы 116 был отклонен со статусом "
            f"{response.status_code}"
        )
        return

    if response.status_code < 500:
        print(
            f"Некорректный payload формы 116 получил неожиданный статус "
            f"{response.status_code}"
        )
        return

    print(
        f"Серверная ошибка на некорректном payload формы 116: "
        f"{response.status_code}"
    )
