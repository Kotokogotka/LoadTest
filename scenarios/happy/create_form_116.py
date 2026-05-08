from payloads.form_116.valid import build_form_116_payload


def create_form_116(user) -> None:
    payload = build_form_116_payload()
    response = user.forms_client.create_form(payload, user.access_token)

    if response.status_code == 200:
        print(f"Пользователь {user.username} создал запись в форме 116")
        return

    print(f"Ошибка создания формы 116, status_code {response.status_code}")
