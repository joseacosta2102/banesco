from pydantic import BaseModel


class RegisterC2pModel(BaseModel):
    enterprise_name: str
