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
