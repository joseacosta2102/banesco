from dotenv import load_dotenv
import os

from enviroments import clients

load_dotenv()

PORT = int(os.getenv("PORT"))
DEV = bool(os.getenv("DEV"))
HOST = str(os.getenv("HOST"))
BASE_URL_TESORO = str(os.getenv("BASE_URL_TESORO"))


def get_enviroment_client(client: str) -> dict:
    return clients.get(client)
