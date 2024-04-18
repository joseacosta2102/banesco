from settings import URL_BANESCO_PAY, URL_BANESCO_CONFIRM_PAY
from requests import request


def pay_request(data: dict):
    return request(
        method="POST",
        url=URL_BANESCO_PAY,
        data=data,
        headers={
            "Content-Type": "application/x-www-form-urlencoded",
        },
        timeout=8,
    )


def confirm_requests(data: dict):
    return request(method="POST", url=URL_BANESCO_CONFIRM_PAY, data=data, timeout=8)
