from pydantic import BaseModel


class PayC2pModel(BaseModel):
    amount: float
    phone: str
    dni: str
    bank: str
    token: str
    enterprise_name: str
    concept: str
