import asyncio

from client.client import Client
from utils.logger import BASE_DIR


async def start_app():
    await application.setup_app(config_path=BASE_DIR / "client" / "config.cfg")
    await application.run()


application: Client = Client()
if __name__ == "__main__":
    try:
        asyncio.run(main=start_app())
    except KeyboardInterrupt:
        print("\nClient stopped")
    except Exception as ex:
        print(f"\n{ex}")
    finally:
        application.logger.stop()



