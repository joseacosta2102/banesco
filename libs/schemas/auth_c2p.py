from pydantic import BaseModel


class AuthC2pModel(BaseModel):
    dni: str
    enterprise_name: str
