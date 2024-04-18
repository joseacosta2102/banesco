from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from services.pay_c2p import pay
from libs.schemas.pay_c2p import PayC2pModel
from settings import get_enviroment_client


router = APIRouter()


@router.post("/pay")
async def create_mobile_payment(payment: PayC2pModel, req: Request):
    client = get_enviroment_client(payment.enterprise_name)

    invalid_client = not client or client["API_KEY"] != req.headers.get("x-api-key")

    if invalid_client:
        return JSONResponse(
            status_code=401,
            content=jsonable_encoder(
                {
                    "error": {
                        "message": "API KEY invalida o cliente no registrado",
                        "code": "0418",
                    }
                }
            ),
        )

    payment = pay(payment)

    if payment.get("error").get("code") == 503:
        return JSONResponse(status_code=503, content=jsonable_encoder(payment))

    return payment
