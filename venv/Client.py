import socket
import asyncio
import time


class ClientError(Exception):
  pass


class Client:

    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeot = timeout

    def put(self, metric, metric_value, timestamp=None):
        try:
            async def tcp_client(message, loop):
                reader, writer = await asyncio.open_connection("127.0.0.1", 10000, loop=loop)
                writer.write(message.encode())
                writer.close()

            if timestamp is None:
                timestamp = str(int(time.time()))
            loop = asyncio.get_event_loop()
            try:
                message = (str(metric) + str(float(metric_value)) + str(int(timestamp)))
            except ValueError:
                print("Bad data")
            loop.run_until_complete(tcp_client(message, loop))
            loop.close()
        except ConnectionRefusedError:
            raise ClientError("Bad Connection") from None



    def get(self, key):
        pass


client = Client("127.0.0.1", 8888, timeout=15)
client.put("palm.cpu", 0.5, timestamp=1150864247)
