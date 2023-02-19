import asyncio

from server.server import Server
from utils.logger import BASE_DIR


async def start_app():
    await application.setup_app(config_path=BASE_DIR / "server" / "config.cfg")
    await application.run()


application: Server = Server()
if __name__ == "__main__":
    try:
        asyncio.run(main=start_app())
    except KeyboardInterrupt:
        print("\nServer stopped")
    except Exception as ex:
        print(f"\n{ex}")
    finally:
        application.logger.stop()
