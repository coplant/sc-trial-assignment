import asyncio

from server.server import Server
from utils.logger import BASE_DIR


async def start_app():
    application: Server = Server()
    await application.setup_app(config_path=BASE_DIR / "server" / "config.cfg")
    await application.run()


if __name__ == "__main__":
    asyncio.run(start_app())
