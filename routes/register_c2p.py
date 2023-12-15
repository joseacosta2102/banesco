from fastapi import APIRouter, Request, Response
from services.register_c2p import register_c2p_tesoro
from libs.schemas.register_c2p import RegisterC2pModel
from settings import get_enviroment_client


router = APIRouter()


@router.post("/vueltodigital/register")
async def register_mobile_payment(register_data: RegisterC2pModel, req: Request):
    client = get_enviroment_client(register_data.enterprise_name)

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

    return register_c2p_tesoro(register_data)
