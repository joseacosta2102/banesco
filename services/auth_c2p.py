from libs.http.base_request import post_request
from libs.schemas.auth_c2p import AuthC2pModel
from utils.requests import request_auth_c2p_object
from utils.responses import format_bank_response


def auth_c2p_tesoro(data: AuthC2pModel):
    data_dict = data.model_dump()
    pay_formated = request_auth_c2p_object(data_dict)

    pay = post_request(data=pay_formated, route="/lotes/solicitud/clave")

    error = pay["codResp"] == "P2P0001"

    if error:
        return format_bank_response(
            message="BANK ERROR",
            error={"message": pay["descResp"], "code": pay["codResp"]},
        )

    return format_bank_response(message="SUCCESS", data=pay)
