import socket

class realtime:
    def __init__(self, host_ip:str='127.0.0.1'):
        self.host = host_ip
        self.port = 30003
        self._init_socket()

    def _init_socket(self):
        self.realtime_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.realtime_socket.connect((self.host, self.port))

    def send_and_receive(self, command:str) -> str:
        self.realtime_socket.send(command.encode('utf-8'))
        return self.realtime_socket.recv(4096).decode('utf-8')