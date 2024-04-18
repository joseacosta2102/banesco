from dotenv import load_dotenv
import os

from enviroments import clients

load_dotenv()

PORT = int(os.getenv("PORT"))
DEV = bool(os.getenv("DEV"))
HOST = str(os.getenv("HOST"))
URL_BANESCO_PAY = str(os.getenv("URL_BANESCO_PAY"))
URL_BANESCO_CONFIRM_PAY = str(os.getenv("URL_BANESCO_CONFIRM_PAY"))


def get_enviroment_client(client: str) -> dict:
    return clients.get(client)
