import socket
import time


class ClientError(Exception):
    pass


class Client:

    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout
        try:
            self.connection = socket.create_connection((host, port), timeout)
        except socket.error as err:
            raise ClientError("error create connection", err)

    def put(self, key, value, timestamp=None):
        if timestamp is None:  # если пользователь не ввёл время, делаем это за него
            timestamp = str(int(time.time()))
        try:
            with socket.create_connection((self.host, self.port), self.timeout) as sock:  # создаём соединение
                string = "put" + str(key) + str(value) + str(timestamp) + "\n"
                sock.sendall(string.encode("utf8"))  # отправляем закодированную строку
                answer = sock.recv(1024).decode("utf8")
                if answer != "ok\n\n":
                    raise ClientError
        except socket.error as err:
            raise ClientError("Cant put(bad connection)")

    def get(self, key):
        try:
            with socket.create_connection((self.host, self.port), self.timeout) as sock:
                answer = sock.recv(1024).decode("utf8")  # получаем даунные с сервера
                items = answer.split("\n")  # разделяем данные по \n превращая их из строчки в список
                data = {}
                for item in items[0:-1]:  # идём поэлементам списка (по строкам) -1 нужен так как в конце пу
                    item = item.split()  # превращаю строку в список слов
                    if item[1] not in data:  # item[1] это ключ, item[0] это слово put
                        data[item[1]] = []
                    data[item[1]].append(
                        (item[2], item[3]))  # item[2] это значение ключа item[3] это время отправки данных
        except socket.error as err:
            raise ClientError("Cant read(bad connection)")
        return data
# client = Client("127.0.0.1", 8888, timeout=15)

# client.put("palm.cpu", 0.5, timestamp=1150864247)
