class AuthClient:
    def __init__(self, http_client):
        self.http_client = http_client

    def login(self, username: str, password: str):
        return self.http_client.post(
            url="/auth-be/auth/jwt/login",
            data={
                "username": username,
                "password": password,
            },
            headers={
                "Content-Type": "application/x-www-form-urlencoded",
            },
        )

    def logout(self, access_token: str):
        return self.http_client.post(
            url="/auth-be/auth/jwt/logout",
            headers={
                "Authorization": f"Bearer {access_token}",
            },
        )

