from libs.http.base_request import post_request
from libs.schemas.register_c2p import RegisterC2pModel
from utils.requests import request_register_c2p_object


def register_c2p_tesoro(data: RegisterC2pModel):
    data_dict = data.model_dump()
    pay_formated = request_register_c2p_object(data_dict)

    return post_request(data=pay_formated, route="/vueltodigital/register")
