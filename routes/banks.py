from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from services.banks import get_banks_service
from libs.schemas.banks import BanksModel
from settings import get_enviroment_client


router = APIRouter()


@router.get("/banks")
async def get_banks(payment: BanksModel, req: Request):
    client = get_enviroment_client(payment.enterprise_name)

    invalid_client = not client or client["API_KEY"] != req.headers.get("x-api-key")

    if invalid_client:
        return JSONResponse(
            status_code=401,
            content=str(
                {
                    "error": {
                        "message": "API KEY invalida o cliente no registrado",
                        "code": "0418",
                    },
                }
            ),
        )

    return get_banks_service()
