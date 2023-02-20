import asyncio
import json

from aioconsole import ainput, aprint
from typing import Optional

import aiofiles
from utils.setup import SetupApplication


class Client(SetupApplication):
    def __init__(self):
        super().__init__()
        self.data: Optional[str] = None

    async def get_menu(self):
        menu = None
        while not menu:
            menu = await ainput(
                """
                1. Keyboard
                2. File
                """
            )
            if menu == "1":
                self.data = await ainput("Math expression: ")
            elif menu == "2":
                path_file: str = await ainput("File path: ")
                try:
                    path_file = path_file.strip().replace("'", "")
                    async with aiofiles.open(path_file, "r") as file:
                        self.data: str = await file.read()
                        self.data = self.data.strip()
                except Exception as message:
                    await aprint(message)
                    self.logger.logger.error(message)
                    menu = None
            else:
                menu = None

    async def run(self):
        reader, writer = await asyncio.open_connection(
            host=self.config.connection.host,
            port=self.config.connection.port
        )

        await self.get_menu()
        if not self.data:
            self.logger.logger.error("No data found")
            return
        self.logger.logger.info(f"Input data: {self.data}")

        try:
            to = {"expression": self.data}
            writer.write(json.dumps(to).encode())
            await writer.drain()
            await aprint(f"Send: {json.dumps(to)}")
            self.logger.logger.info(f"Send: {json.dumps(to)}")
        except ValueError as exception:
            self.logger.logger.error(f"{exception!r}")
            print(f"{exception!r}")

        data = await reader.read(100)
        data = json.loads(data.decode())
        await aprint(f"Received: {data}")
        self.logger.logger.info(f"Received: {data}")

        await aprint(f"Result: {data.get('result')}")
        self.logger.logger.info(f"Result: {data.get('result')}")

        await aprint("Close the connection")
        self.logger.logger.info("Close the connection")
        writer.close()
        await writer.wait_closed()
