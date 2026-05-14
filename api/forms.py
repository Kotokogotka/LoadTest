class FormsClient:
    def __init__(self, http_client):
        self.http_client = http_client

    def open_form(self, form_id: int, access_token: str):
        return self.http_client.get(
            url=f"/constructor/ankets/{form_id}",
            headers={
                "Authorization": f"Bearer {access_token}",
            },
        )

    def open_arm(self, arm_path: str, access_token: str):
        return self.http_client.get(
            url=arm_path,
            headers={
                "Authorization": f"Bearer {access_token}",
            },
        )

    def create_form(self, payload: dict, access_token: str):
        return self.http_client.post(
            url="/constructor-be/anket/",
            json=payload,
            headers={
                "Authorization": f"Bearer {access_token}",
            },
        )

    def patch_form(self, anket_id: int, payload: dict, access_token: str):
        return self.http_client.patch(
            url=f"/constructor-be/anket/{anket_id}",
            json=payload,
            headers={"Authorization": f"Bearer {access_token}"},
        )

    def soft_delete_form(self, anket_id: int, access_token: str):
        return self.patch_form(
            anket_id=anket_id,
            payload={"is_active": False},
            access_token=access_token,
        )
