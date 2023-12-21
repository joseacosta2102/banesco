from libs.http.base_request import post_request
from libs.schemas.confirm_c2p import ConfirmC2pModel
from utils.requests import request_confirm_c2p_object
from utils.responses import format_bank_response


def confirm_c2p_tesoro(data: ConfirmC2pModel):
    data_dict = data.model_dump()
    pay_formated = request_confirm_c2p_object(data_dict)

    pay = post_request(data=pay_formated, route="/BotonDePago/Conformacion")

    error = pay["status"] == "Error"

    if error:
        return format_bank_response(
            error={"message": pay["mensaje"], "code": "TES0001"}, message="BANK ERROR"
        )

    return format_bank_response(data=pay, message="SUCCESS")
