from libs.http.base_request import post_request
from utils.responses import format_bank_response


def get_banks_service():
    banks = post_request(route="/bancos", data={})
    return format_bank_response(data={"banks": banks}, message="SUCCESS")
