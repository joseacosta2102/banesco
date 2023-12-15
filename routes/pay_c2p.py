from fastapi import APIRouter, Request, Response
from services.pay_c2p import pay_c2p_tesoro
from libs.schemas.pay_c2p import PayC2pModel
from settings import get_enviroment_client


router = APIRouter()


@router.post("/vueltodigital/transaccion/merchantbt")
async def create_mobile_payment(payment: PayC2pModel, req: Request):
    client = get_enviroment_client(payment.enterprise_name)

    if not client or client["API_KEY"] != req.headers.get("x-api-key"):
        return Response(
            status_code=401,
            content=str(
                {
                    "message": "API KEY invalida o cliente no registrado",
                    "code": "0418",
                }
            ),
        )
    return pay_c2p_tesoro(payment)
