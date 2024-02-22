import socket


class ClientSocket:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket()

    def __start_server(self):
        self.socket.connect((self.host, self.port))
        self.print_info(f"Connection from client has been established! Host: {self.host}, Port: {self.port}")

    def start(self):
        self.__start_server()
        self.__listener()

    def __listener(self):
        message = input("type command for ex.: exchange 1 PLN -> ")

        while message.lower().strip() != 'q':
            self.socket.send(message.encode())

            msg = self.socket.recv(1024).decode()

            self.print_info(f"Received message: {msg}")
            message = input("type command for ex.: exchange 1 PLN -> ")

        self.__stop_client()

    def __stop_client(self):
        self.socket.close()

    def print_info(self, text):
        print(text)


def main():
    client_socket = ClientSocket(socket.gethostbyname('localhost'), 4001)
    client_socket.start()


if __name__ == '__main__':
    main()
