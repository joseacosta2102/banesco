from fastapi import APIRouter, Request, Response
from services.auth_c2p import auth_c2p_tesoro
from libs.schemas.auth_c2p import AuthC2pModel
from settings import get_enviroment_client


router = APIRouter()


@router.post("/vueltodigital/Authenticate")
async def auth_mobile_payment(payment: AuthC2pModel, req: Request):
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

    return auth_c2p_tesoro(payment)
