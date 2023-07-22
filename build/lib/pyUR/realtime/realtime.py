import socket

'private properties'
_host : str = None
_port : int = None
_realtime_socket : socket = None

'''
class for realtime comminucation to universal robot
port 30003
'''
async def __init__():
    pass

'''
function for initialize socket
:param host_ip: ip address of robot
'''
def init_socket(host_ip:str='127.0.0.1'):
    global _host, _port, _realtime_socket
    _host = host_ip
    _port = 30003
    _realtime_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    _realtime_socket.connect((_host, _port))

'''
send command to robot
:param command: command to send
'''
def send(command:str):
    global _realtime_socket
    _realtime_socket.send(command.encode('utf-8'))

'''
receive status from robot
'''
def receive_status() -> bytearray:
    global _realtime_socket
    return _realtime_socket.recv(4096)
    