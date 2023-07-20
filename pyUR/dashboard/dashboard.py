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

'''
function for initialize socket
:param host_ip: ip address of robot
'''
def init_socket(host_ip:str='127.0.0.1'):
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

'''
function for send/receive to socket
:param dashboard_command: command to send to the robot
'''
def send_receive_socket(dashboard_command:str) -> str:
    global _dashboard_socket
    try:
        print(dashboard_command)
        _dashboard_socket.send(dashboard_command.encode('utf-8'))
        return str(_dashboard_socket.recv(1024).decode('utf-8'))
    except:
        return None

