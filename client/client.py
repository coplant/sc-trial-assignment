import asyncio
import json
from typing import Optional

from utils.setup import SetupApplication


class Client(SetupApplication):
    def __init__(self):
        super().__init__()

    # TODO: Where to load from
    # TODO: JSON?
    # TODO: Reversed Polish Notation (class-solver?)
    # FIXME: OSError - incorrect connection address
    async def run(self):  # TODO: Logging
        reader, writer = await asyncio.open_connection(
            host=self.config.connection.host,
            port=self.config.connection.port
        )
        message = '123'
        print(f'Send: {message!r}')
        writer.write(message.encode())
        await writer.drain()

        data = await reader.read(100)
        print(f'Received: {data.decode()!r}')
        print('Close the connection')
        writer.close()
        await writer.wait_closed()
