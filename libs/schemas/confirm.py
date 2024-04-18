from pydantic import BaseModel


class ConfirmModel(BaseModel):
    transaction: str
    enterprise_name: str
