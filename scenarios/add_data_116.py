from data.generate_data_116 import generate_form_116_full

def add_new_data_116(user):
    payload = generate_form_116_full()

    response = user.client.post(
        url="/constructor-be/anket/",
        json=payload,
        headers={"Authorization": f"Bearer {user.access_token}"}
    )

    if response.status_code == 200:
        print(f"Пользователь {user.username} создал запись в форме 116")
    else:
        print(f"Ошибка, status_code {response.status_code}")