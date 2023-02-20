import asyncio
import json
from typing import Optional

from aioconsole import aprint

from utils.notation import MathExpression
from utils.setup import SetupApplication


class Server(SetupApplication):
    def __init__(self):
        super().__init__()

    async def write(self, writer, message):
        writer.write(message)
        await writer.drain()
        await aprint(f"Send: {message!r}")
        self.logger.logger.info(f"Send: {message!r}")

    async def close(self, writer):
        writer.close()
        await writer.wait_closed()
        await aprint("Close the connection")
        self.logger.logger.info(f"Close the connection")

    async def run(self):
        server = await asyncio.start_server(
            self.handle_message,
            host=self.config.connection.host,
            port=self.config.connection.port
        )

        addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
        await aprint(f'Serving on {addrs}')
        self.logger.logger.info(f'Serving on {addrs}')
        async with server:
            await server.serve_forever()

    async def handle_message(self, reader, writer):
        expression: Optional[MathExpression] = None
        addr = writer.get_extra_info('peername')
        data = await reader.read(100)
        message = json.loads(data.decode())
        await aprint(f"Received {message!r} from {addr!r}")
        self.logger.logger.info(f"Received {message!r} from {addr!r}")

        if isinstance(message, dict):
            data = message.get("expression")
        expression = MathExpression(data)
        await aprint(f"Parsed rpn: {expression}")
        self.logger.logger.info(f"Parsed rpn: {expression}")
        expression = MathExpression(data)
        try:
            to = expression.evaluate()
        except Exception as e:
            to = f"Internal Server Error: {e}"

        await aprint(f"Solved expression: {to}")
        self.logger.logger.info(f"Solved expression: {to}")
        await self.write(writer, json.dumps({"result": to}).encode())
        await self.close(writer)
