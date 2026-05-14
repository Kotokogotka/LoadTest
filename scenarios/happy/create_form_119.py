from payloads.form_119.valid import build_form_119_payload


def create_form_119(user) -> None:
    payload = build_form_119_payload()
    response = user.forms_client.create_form(payload, user.access_token)

    if response.status_code != 200:
        print(f"Ошибка создания анкеты в форме 119, ERROR {response.status_code}")
        return None

    created = response.json()
    anket_id = created.get("id")

    if not anket_id:
        print("Не удалось получить id созданной анкеты в форме 119")
        return None

    print(f"Пользователь {user.username} создал анкету в форме 119 id: {anket_id} ")
    return anket_id


def create_and_soft_delete_form_119(user) -> None:
    anket_id = create_form_119(user)
    if not anket_id:
        return

    patch_response = user.forms_client.soft_delete_form(anket_id, user.access_token)

    if patch_response.status_code in (200, 202, 204):
        print(f"Анкета 119 мягко удалена: id={anket_id}")
        return

    print(f"Ошибка soft delete формы 119 id={anket_id}, status_code {patch_response.status_code}")
