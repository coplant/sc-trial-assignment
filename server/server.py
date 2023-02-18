import asyncio
import json
from typing import Optional

from utils.setup import SetupApplication


class Server(SetupApplication):
    def __init__(self):
        super().__init__()

    async def run(self):  # TODO: Logging
        server = await asyncio.start_server(
            self.handle_echo,
            host=self.config.connection.host,
            port=self.config.connection.port

        )

        addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
        print(f'Serving on {addrs}')
        async with server:
            await server.serve_forever()

    @staticmethod
    async def handle_echo(reader, writer):
        data = await reader.read(100)
        message = data.decode()
        addr = writer.get_extra_info('peername')

        print(f"Received {message!r} from {addr!r}")
        print(f"Send: {message!r}")
        writer.write(data)
        await writer.drain()
        print("Close the connection")
        writer.close()
        await writer.wait_closed()

