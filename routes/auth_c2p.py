from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from services.auth_c2p import auth_c2p_tesoro
from libs.schemas.auth_c2p import AuthC2pModel
from settings import get_enviroment_client


router = APIRouter()


@router.post("/pay/auth")
async def auth_mobile_payment(payment: AuthC2pModel, req: Request):
    client = get_enviroment_client(payment.enterprise_name)

    invalid_client = not client or client["API_KEY"] != req.headers.get("x-api-key")

    if invalid_client:
        return JSONResponse(
            status_code=401,
            content={
                "error": {
                    "message": "API KEY invalida o cliente no registrado",
                    "code": "0418",
                }
            },
        )

    pay = auth_c2p_tesoro(payment)

    can_error = bool(pay["error"])

    if can_error:
        return JSONResponse(status_code=502, content=pay)

    return pay
