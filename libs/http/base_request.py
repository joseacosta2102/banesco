from pyxios import Pyxios
from settings import BASE_URL_TESORO

tesoro = Pyxios(BASE_URL_TESORO, timeout=5)


def post_request(route: str, data: dict):
    return tesoro.post(url=route, headers=data).json()
