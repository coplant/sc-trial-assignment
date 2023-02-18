import asyncio

from client.client import Client
from utils.logger import BASE_DIR


async def start_app():
    application: Client = Client()
    await application.setup_app(config_path=BASE_DIR / "client" / "config.cfg")


if __name__ == "__main__":
    asyncio.run(start_app())
