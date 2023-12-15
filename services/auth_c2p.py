from libs.http.base_request import post_request
from libs.schemas.auth_c2p import AuthC2pModel
from utils.requests import request_auth_c2p_object


def auth_c2p_tesoro(data: AuthC2pModel):
    data_dict = data.model_dump()
    pay_formated = request_auth_c2p_object(data_dict)

    has_error = pay_formated.get("De Error")

    if has_error:
        return has_error

    return post_request(data=pay_formated, route="/vueltodigital/Authenticate")
