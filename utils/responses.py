def format_bank_response(data: dict = {}, message: str = "", error: dict = {}) -> dict:
    return {"data": data, "message": message, "error": error}
