import socket

'private properties'
_host : str = None
_port : int = None
_realtime_socket : socket = None

async def __init__():
    pass

def init_socket(host_ip:str='127.0.0.1'):
    '''
    function for initialize socket
    :param host_ip: ip address of robot
    '''
    global _host, _port, _realtime_socket
    _host = host_ip
    _port = 30003
    _realtime_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    _realtime_socket.connect((_host, _port))

def send(command:str):
    '''
    send command to robot
    :param command: command to send
    '''
    global _realtime_socket
    _realtime_socket.send(command.encode('utf-8'))

def receive_status() -> bytearray:
    '''
    receive status from robot
    '''
    global _realtime_socket
    return _realtime_socket.recv(4096)
    