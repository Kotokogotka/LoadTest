from pydantic import BaseModel


class StoredAccount(BaseModel):
    alias: str
    username: str
    rid: str


class RuntimeAccount(BaseModel):
    alias: str
    username: str
    password: str
    rid: str
