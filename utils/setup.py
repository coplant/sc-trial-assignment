import json
from typing import Optional

import aiofiles

from utils.config import Config, Connection
from utils.logger import AsyncLogger


class SetupApplication:
    def __init__(self):
        self.config: Optional[Config] = None
        self.logger: Optional[AsyncLogger] = None

    def __del__(self):
        if self.logger:
            self.logger.stop()

    async def setup_app(self, config_path):
        await self._setup_config(config_path)
        await self._setup_logging()

    async def _setup_logging(self):
        if not self.logger:
            self.logger = AsyncLogger(self.config.name)
            self.logger.start()

    async def _setup_config(self, config_path):
        try:
            async with aiofiles.open(config_path, "r") as file:
                raw: str = await file.read()
        except IOError as e:
            if not self.logger:
                await self._setup_logging()
            self.logger.logger.error(e)
        try:
            data: dict = json.loads(raw)
            self.config = Config(connection=Connection(
                host=data.get("connection").get("host"),
                port=data.get("connection").get("port")),
                name=data.get("name")
            )
        except Exception as e:
            if not self.logger:
                await self._setup_logging()
            self.logger.logger.error(e)
