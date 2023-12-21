from settings import (
    HOST,
    get_enviroment_client,
)


def request_confirm_c2p_object(find_object: dict) -> dict:
    client = get_enviroment_client(find_object["enterprise_name"])

    return {
        "referencia": find_object["reference"],
        "monto": find_object["amount"],
        "celular": find_object["phone"],
        "banco": find_object["bank"],
        "fecha": find_object["date"],
        "codAfiliado": client["CODE"],
        "RIF": client["VAT"],
    }


def request_pay_c2p_object(pay_object: dict) -> dict:
    client = get_enviroment_client(pay_object["enterprise_name"])

    return {
        "canal": "06",
        "cedular": pay_object["phone"],
        "banco": pay_object["bank"],
        "cedula": pay_object["dni"],
        "monto": pay_object["amount"],
        "token": pay_object["token"],
        "concepto": pay_object["concept"],
        "RIF": client["VAT"],
        "codAfiliado": client["CODE"],
        "comercio": "",
    }


def request_auth_c2p_object(pay_object: dict) -> dict:
    return {"canal": "01", "celularDestino": pay_object["dni"]}
