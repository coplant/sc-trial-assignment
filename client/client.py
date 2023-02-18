import json
from typing import Optional
import aiofiles

from client.config import Config, Connection
from utils.logger import AsyncLogger


class Client:
    def __init__(self):
        self.config: Optional[Config] = None
        self.logger: Optional[AsyncLogger] = None

    def __del__(self):
        if self.logger:
            self.logger.stop()

    async def setup_app(self, config_path):
        await self._setup_logging()
        await self._setup_config(config_path)

    async def _setup_logging(self):
        if not self.logger:
            self.logger = AsyncLogger("client")  # TODO: имя из .cfg
            self.logger.start()

    async def _setup_config(self, config_path):
        try:
            async with aiofiles.open(config_path, "r") as file:
                raw: str = await file.read()
        except IOError as e:
            self.logger.logger.error(e)
        try:
            data: dict = json.loads(raw)
            self.config = Config(Connection(host=data.get("host"), port=data.get("port")))
        except json.JSONDecodeError as e:
            self.logger.logger.error(e)
        except Exception as e:
            self.logger.logger.error(e)
