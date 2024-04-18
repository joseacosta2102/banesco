from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from services.confirm import confirm
from libs.schemas.confirm import ConfirmModel
from settings import get_enviroment_client


router = APIRouter()


@router.post("/confirm")
async def confirm_payment(payment: ConfirmModel, req: Request):
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

    pay = confirm(payment)

    if not pay.get("error").get("code"):
        return pay

    return JSONResponse(
        status_code=pay.get("error").get("code"), content=jsonable_encoder(pay)
    )
