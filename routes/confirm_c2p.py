from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from services.confirm_c2p import confirm_c2p_tesoro
from libs.schemas.confirm_c2p import ConfirmC2pModel
from settings import get_enviroment_client


router = APIRouter()


@router.post("/pay/confirm")
async def confirm_mobile_payment(register_data: ConfirmC2pModel, req: Request):
    client = get_enviroment_client(register_data.enterprise_name)

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

    confirm = confirm_c2p_tesoro(register_data)

    can_error = bool(confirm["error"])

    if can_error:
        return JSONResponse(status_code=502, content=confirm)

    return confirm
