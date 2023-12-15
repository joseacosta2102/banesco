from pydantic import BaseModel


class AuthC2pModel(BaseModel):
    username: str
    password: str
    enterprise_name: str
