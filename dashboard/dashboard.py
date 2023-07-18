import socket
global status 
status = {
    "online": False,
    "booting": False,
    "servo_on": False,
    "break_released": False,
    "robot_is_ready": False,
    "program_loaded": False,
    "program_playing": False,
    "program_paused": False,
    "program_stopped": False,
} 
'''
init
'''
def __init__(self, host_ip):
    self.host = host_ip
    self.port = 20000
    _init_socket(self)

def _init_socket(self):
    self.dashboard_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.dashboard_socket.connect((self.host, self.port))
    status["online"] = True

'''
function for send/receive to socket
'''
def send_receive_socket(self, dashboard_command:str) -> str:
    try:
        self.dashboard_socket.send(dashboard_command)
        return self.dashboard_socket.recv(1024)
    except:
        return None
    
'''
function for parsing status of the robot
'''
def parse_status(self, status:str) -> dict:
    status = status.decode("utf-8").split(" ")
    status_dict = {}
    for i in range(0, len(status), 2):
        status_dict[status[i]] = status[i+1]
    return status_dict
