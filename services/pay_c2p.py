from libs.http.base_request import post_request
from libs.schemas.pay_c2p import PayC2pModel
from utils.requests import request_pay_c2p_object


def pay_c2p_tesoro(data: PayC2pModel):
    data_dict = data.model_dump()
    pay_formated = request_pay_c2p_object(data_dict)

    return post_request(
        data=pay_formated, route="/vueltodigital/transaccion/merchantbt"
    )
