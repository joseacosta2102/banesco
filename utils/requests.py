import hmac
import hashlib
import base64

from settings import (
    HOST,
    get_enviroment_client,
)


def sign_sha256(string: str, secret: str) -> str:
    return hmac.new(secret.encode(), string.encode(), hashlib.sha256).hexdigest()


def request_pay_object(pay_object: dict) -> dict:
    client = get_enviroment_client(pay_object["enterprise_name"])

    hash_str_values = f"{client['API_KEY_BANESCO']}{pay_object['vat']}{pay_object['amount']}01{pay_object['transaction']}"

    sign = sign_sha256(secret=client["SECRET"], string=hash_str_values)

    return {
        "valor1": pay_object["vat"],
        "valor2": pay_object["amount"],
        "valor3": "01",
        "valor4": pay_object["transaction"],
        "valor5": pay_object["concept"],
        "apikey": client["API_KEY_BANESCO"],
        "firma": sign,
        "tipo": 1,
    }


def request_confirm_object(pay_object: dict) -> dict:
    client = get_enviroment_client(pay_object["enterprise_name"])

    hash_str_values = f"{client['API_KEY_BANESCO']}{pay_object['transaction']}"

    sign = sign_sha256(secret=client["SECRET"], string=hash_str_values)

    value = str(
        {
            "apiKey": client["API_KEY_BANESCO"],
            "firma": sign,
            "nroComprobante": pay_object["transaction"],
        }
    ).encode()

    return base64.b64encode(value)
