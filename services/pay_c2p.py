from bs4 import BeautifulSoup
from libs.http.base_request import pay_request
from libs.schemas.pay_c2p import PayC2pModel
from utils.requests import request_pay_object
from utils.responses import format_bank_response


def pay(data: PayC2pModel):
    data_dict = data.model_dump()
    pay_formated = request_pay_object(data_dict)

    pay = pay_request(data=pay_formated)

    print(pay.text)

    soup = BeautifulSoup(pay.text, "html.parser")

    title = soup.find(id="titulobarra").text

    description = soup.find(id="span_error").text

    error = {"message": description, "code": 503}

    return format_bank_response(message=title, error=error)
