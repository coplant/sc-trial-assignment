import asyncio
import json
from typing import Optional

from utils.setup import SetupApplication


class Server(SetupApplication):
    def __init__(self):
        super().__init__()

    async def run(self):
        reader, writer = await asyncio.open_connection(
            host=self.config.connection.host,
            port=self.config.connection.port
        )
