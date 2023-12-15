from settings import (
    HOST,
    get_enviroment_client,
)


def request_register_c2p_object(find_object: dict) -> dict:
    client = get_enviroment_client(find_object["enterprise_name"])

    return {
        "username": client["PHONE"],
        "password": client["PASSWORD"],
        "ctaOri": client["ACCOUNT"],
        "tlfOri": client["PHONE"],
    }


def request_pay_c2p_object(pay_object: dict) -> dict:
    client = get_enviroment_client(pay_object["enterprise_name"])

    return {
        "idAliado": pay_object["partner_id"],
        "idPost": pay_object["post_id"],
        "ctaDeb": client["ACCOUNT"],
        "idEmpresa": client["VAT"],
        "tlfDeb": client["PHONE"],
        "idCliente": pay_object["client_vat"],
        "monto": pay_object["amount"],
        "telefono": pay_object["client_phone"],
        "cod_banco": pay_object["auth_bank_code"],
    }


def request_auth_c2p_object(pay_object: dict) -> dict:
    client = get_enviroment_client(pay_object["enterprise_name"])

    is_valid_auth_fields = (
        client["PASSWORD"] == pay_object["password"]
        and client["username"] == pay_object["username"]
    )

    if not is_valid_auth_fields:
        return {"De Error": "datos de autenticacion invalidos"}

    return {"username": pay_object["username"], "password": pay_object["password"]}
