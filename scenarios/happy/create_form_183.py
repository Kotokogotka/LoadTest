from payloads.form_183.valid import build_form_183_payload

def create_form_183(user):
    payload = build_form_183_payload()

    response = user.forms_client.create_form(payload, user.access_token)

    if response.status_code == 200:
        print(f"Пользователь {user.username} создал запись в форме 183")
        return

    print(f"Ошибка создания формы 116, status_code {response.status_code}")