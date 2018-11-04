import socket
import time


class ClientError(Exception):
    pass


class Client:

    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout

    def put(self, key, value, timestamp=None):
        if timestamp is None:
            timestamp = str(int(time.time()))
        with socket.create_connection((self.host, self.port), self.timeout) as sock:
            string = "put" + str(key) + str(value) + str(timestamp) + "\n"
            sock.sendall(string.encode("utf8"))
            answer = sock.recv(1024).decode("utf8")
            if answer != "ok\n\n":
                raise ClientError

    def get(self, key):
        with socket.create_connection((self.host, self.port), self.timeout) as sock:
            answer=sock.recv(1024).decode("utf8")
            print(answer)


client = Client("127.0.0.1", 8888, timeout=15)

client.put("palm.cpu", 0.5, timestamp=1150864247)
