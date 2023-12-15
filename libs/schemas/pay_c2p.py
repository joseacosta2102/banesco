from pydantic import BaseModel


class PayC2pModel(BaseModel):
    amount: float
    client_phone: str
    client_vat: str
    post_id: str
    auth_bank_code: str
    enterprise_name: str
    partner_id: int
