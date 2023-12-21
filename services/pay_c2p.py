from libs.http.base_request import post_request
from libs.schemas.pay_c2p import PayC2pModel
from utils.requests import request_pay_c2p_object
from utils.responses import format_bank_response


def pay_c2p_tesoro(data: PayC2pModel):
    data_dict = data.model_dump()
    pay_formated = request_pay_c2p_object(data_dict)

    pay = post_request(data=pay_formated, route="/botonDePago/pago")

    error = pay["codres"] == "P2P0001"

    if error:
        return format_bank_response(
            message="BANK ERROR",
            error={"message": pay["descRes"], "code": pay["codres"]},
        )

    return format_bank_response(message="SUCCESS", data=pay)
