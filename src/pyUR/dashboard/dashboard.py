import socket

'private properties'
_host : str = None
_port : int = None
_dashboard_socket : socket = None
_connected : bool = False

'''
class for dashboard comminucation
port 29999
'''
def __init__(self):
    pass

def init_socket(host_ip:str='127.0.0.1'):
    '''
    function for initialize socket
    :param host_ip: ip address of robot
    '''
    global _host, _port, _dashboard_socket, _connected
    _host = host_ip
    _port = 29999
    _dashboard_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    _dashboard_socket.connect((_host, _port))
    connected = _dashboard_socket.recv(1024).decode('utf-8')
    if 'Connected' in connected:
        _connected = True
        print('Dashboard connected')
    else :
        _connected = False
    
def is_connected() -> bool:
    global _connected
    return _connected

def send_receive_socket(dashboard_command:str) -> str:
    '''
    function for send/receive to socket
    :param dashboard_command: command to send to the robot
    '''
    global _dashboard_socket
    try:
        send_socket(dashboard_command)
        return receive_socket()
    except:
        return None
    
def send_socket(dashboard_command:str) -> None:
    '''
    function for send to socket
    :param dashboard_command: command to send to the robot
    '''
    global _dashboard_socket
    try:
        _dashboard_socket.send(dashboard_command.encode('utf-8'))
    except:
        pass

def receive_socket() -> str:  
    '''
    function for receive from socket
    '''
    global _dashboard_socket
    try:
        return str(_dashboard_socket.recv(1024).decode('utf-8'))
    except:
        return None
    

