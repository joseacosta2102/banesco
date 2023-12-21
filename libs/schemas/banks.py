from pydantic import BaseModel


class BanksModel(BaseModel):
    enterprise_name: str
