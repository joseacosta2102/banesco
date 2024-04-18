from pydantic import BaseModel


class PayC2pModel(BaseModel):
    vat: str
    amount: float
    transaction: str
    concept: str
    enterprise_name: str
