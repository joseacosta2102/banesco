from pyxios import Pyxios
from settings import BASE_URL_TESORO

tesoro = Pyxios(BASE_URL_TESORO, timeout=5)


def post_request(route: str, data: dict):
    fetch = tesoro.post(url=route, json=data)
    is_not_found = fetch.status_code == 404

    if is_not_found:
        return {"mensaje": "RECURSO NO ENCONTRADO", "usuario": None, "status": "Error"}

    return tesoro.post(url=route, json=data).json()
