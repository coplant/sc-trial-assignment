import asyncio
from asyncio import AbstractEventLoop
from typing import Optional

from client.client import Client
from utils.logger import BASE_DIR


async def start_app():
    application: Client = Client()
    await application.setup_app(config_path=BASE_DIR / "client" / "config.cfg")
    await application.run()


if __name__ == "__main__":
    asyncio.run(start_app())

    # loop: Optional[AbstractEventLoop] = asyncio.get_event_loop()
    # try:
    #     loop.run_until_complete(start_app())
    # except KeyboardInterrupt:
    #     print("It's ok")
    # finally:
    #     loop.stop()
    #     loop.close()

    # try:
    #     asyncio.run(start_app())
    # except KeyboardInterrupt as message:
    #     print(message)
    # finally:
    #     loop.stop()
    #     loop.close()
