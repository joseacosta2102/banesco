from libs.http.base_request import confirm_requests
from libs.schemas.confirm import ConfirmModel
from utils.requests import request_confirm_object
from utils.responses import format_bank_response, format_confirm_pay


def confirm(data: ConfirmModel):
    data_dict = data.model_dump()
    pay_formated = request_confirm_object(data_dict)

    confirm = confirm_requests(data=pay_formated).json()

    if confirm.get("estatus") != "00":
        return format_bank_response(
            message="BANESCO ERROR",
            error={"code": 503, "message": confirm.get("mensaje")},
        )

    return format_bank_response(
        message="SUCCESS", data=format_confirm_pay(confirm.get("detalle"))
    )
