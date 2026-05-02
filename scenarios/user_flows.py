import random

FORM_IDS = [116, 223, 119, 165, 183, 224, 255, 232, 141]
ARMS_tails = ['radiation/rm', 'chemistry/rm', 'biology/rm', 'cou/rm', 'map/operational']

def visit_random_form(user) -> None:
    form_id = random.choice(FORM_IDS)

    response = user.client.get(
        url=f"/constructor/ankets/{form_id}",
        headers={
            "Authorization": f"Bearer {user.access_token}",
        },
    )

    if response.status_code == 200:
        print(f"Пользователь {user.username} открыл анкету {form_id}")
    else:
        print(
            f"Ошибка открытия анкеты {form_id} "
            f"для пользователя {user.username}: {response.status_code}"
        )

def visit_random_arm(user) -> None:
    arms_random_tail = random.choice(ARMS_tails)
    if user.account.alias != "u001":
        return
    try:
        response = user.client.get(
            url=f"{arms_random_tail}",
            headers={
                "Authorization": f"Bearer {user.access_token}",
            },
        )
        if response.status_code == 200:
            print(f'Пользователь успешно перешел {arms_random_tail}')
    except Exception as e:
        print(f"Error {e}")
