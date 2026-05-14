import random

FORM_IDS = [116, 223, 119, 165, 183, 224, 255, 232, 141]
ARM_PATHS = [
    "/radiation/rm",
    "/chemistry/rm",
    "/biology/rm",
    "/cou/rm",
    "/map/operational",
]


def open_random_form(user) -> None:
    form_id = random.choice(FORM_IDS)
    response = user.forms_client.open_form(form_id, user.access_token)

    if response.status_code == 200:
        print(f"Пользователь {user.username} открыл анкету {form_id}")
        return

    print(
        f"Ошибка открытия анкеты {form_id} "
        f"для пользователя {user.username}: {response.status_code}"
    )


def open_random_arm(user) -> None:
    if user.account is None or user.account.alias != "u001":
        return

    arm_path = random.choice(ARM_PATHS)

    try:
        response = user.forms_client.open_arm(arm_path, user.access_token)
        if response.status_code == 200:
            print(f"Пользователь успешно перешел {arm_path}")
    except Exception as error:
        print(f"Error {error}")
