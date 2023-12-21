from pydantic import BaseModel


class ConfirmC2pModel(BaseModel):
    enterprise_name: str
    reference: str
    bank: str
    date: str
    phone: str
    amount: str
