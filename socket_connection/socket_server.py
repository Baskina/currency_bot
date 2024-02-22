import socket
import sys

sys.path.append('../..')
from currency_bot.bot import main as get_data


class ServerSocket:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket()

    def __start_socket(self):
        self.socket.bind((self.host, self.port))
        self.socket.listen()
        conn, address = self.socket.accept()
        self.print_info(f"Connection from {address} has been established! Host: {self.host}, Port: {self.port}")
        return conn

    def start(self, action):
        conn = self.__start_socket()
        self.__listener(action, conn)

    def __listener(self, action, connection):
        while True:
            command = connection.recv(1024).decode()
            if not command:
                break
            self.print_info(f"Received message: {command}")
            response = action(command)
            connection.send(response.encode())
        connection.close()
        self.__stop_socket()

    def __stop_socket(self):
        self.socket.close()

    def print_info(self, text):
        print(text)


def main():
    server_socket = ServerSocket(socket.gethostbyname('localhost'), 4001)
    server_socket.start(get_data)


if __name__ == '__main__':
    main()
