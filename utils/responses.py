def format_bank_response(data: dict = {}, message: str = "", error: dict = {}) -> dict:
    return {"data": data, "message": message, "error": error}


def format_confirm_pay(data: dict):
    return {
        "vat": data.get("valor1"),
        "amount": data.get("valor2"),
        "transaction": data.get("valor4"),
        "concept": data.get("valor5"),
        "date": data.get("fecha_pago"),
        "currency": data.get("moneda"),
        "reference": data.get("nro_referencia_banco"),
        "bank": data.get("id_banco_origen"),
    }
