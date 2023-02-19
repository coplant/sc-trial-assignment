import asyncio
import json

import aioconsole
from aioconsole import ainput, aprint
from typing import Optional

import aiofiles

from utils.notation import MathExpression
from utils.setup import SetupApplication


class Client(SetupApplication):
    def __init__(self):
        super().__init__()
        self.data: Optional[str] = None

    # TODO: JSON?
    # TODO: Reversed Polish Notation (class-solver?)
    # FIXME: OSError - incorrect connection address

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
                path_file = await ainput("File path: ")
                try:
                    async with aiofiles.open(path_file, "r") as file:
                        self.data: str = await file.read()
                except Exception as message:
                    await aprint(message)
                    self.logger.logger.error(message)
                    menu = None
            else:
                menu = None

    async def run(self):  # TODO: Logging
        reader, writer = await asyncio.open_connection(
            host=self.config.connection.host,
            port=self.config.connection.port
        )

        await self.get_menu()
        if self.data:
            print(self.data)
        expression = MathExpression()

        # send data to server
        message = '12'
        print(f'Send: {message!r}')
        writer.write(message.encode())
        await writer.drain()

        #recv data from server
        data = await reader.read(100)
        print(f'Received: {data.decode()!r}')
        print('Close the connection')
        writer.close()
        await writer.wait_closed()
