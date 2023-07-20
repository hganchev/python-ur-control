import socket

class dashboard:
    '''
    init
    :param host_ip: ip address of the robot
    '''
    def __init__(self, host_ip:str='127.0.0.1'):
        self.host = host_ip
        self.port = 29999
        self._init_socket()

    def _init_socket(self):
        self.dashboard_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.dashboard_socket.connect((self.host, self.port))
        connected = self.dashboard_socket.recv(1024).decode('utf-8')
        if 'Connected' in connected:
            self.connected = True
            print('Dashboard connected')
        else :
            self.connected = False
        
    def is_connected(self) -> bool:
        return self.connected

    '''
    function for send/receive to socket
    :param dashboard_command: command to send to the robot
    '''
    def send_receive_socket(self, dashboard_command:str) -> str:
        try:
            print(dashboard_command)
            self.dashboard_socket.send(dashboard_command.encode('utf-8'))
            return str(self.dashboard_socket.recv(1024).decode('utf-8'))
        except:
            return None
    
