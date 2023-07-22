import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
from pyUR.dashboard import dashboard, dashboard_commands
from pyUR.realtime import realtime, realtime_commands, realtime_statuses
from time import sleep

'''
init ur control by creating a thread
'''
def __init__():
   pass

'''
init dashboard server and realtime server
:param host_ip: host ip address
'''
def init(host_ip: str='127.0.0.1'):
    # create a dashboard object
    dashboard.init_socket(host_ip=host_ip)
    if dashboard.is_connected():
        print('Connected to UR Dashboard Server')

    # create a realtime object
    realtime.init_socket(host_ip=host_ip)

'''
send power on command
'''
def power_on():
    responce = dashboard.send_receive_socket(dashboard_commands.power_on())
    print(responce)

'''
send brake release command
'''
def break_release():
    responce = dashboard.send_receive_socket(dashboard_commands.brake_release())
    print(responce)

'''
set tcp
:param tcp_offset: tcp offset
'''
def set_tcp(tcp_offset: list=[0, 0, 0, 0, 0, 0]):
    realtime.send(realtime_commands.set_tcp(tcp_offset))

'''
set payload
:param payload: payload in kg
:param cog: center of gravity [CoGx, CoGy, CoGz] specifying the offset (in meters) from the tool mount.
:param inertia: inertia [Ixx, Ixy, Ixz, Iyy, Iyz, Izz]  - in kg*m^2 !can not be negative!
'''
def set_payload(payload: float=0, cog: list=[0, 0, 0], inertia: list=[0,0,0,0,0,0]):
    realtime.send(realtime_commands.set_target_payload(payload, cog, inertia))

'''
move joint with pose
:param pose: pose to move to
:param a: acceleration
:param v: velocity
:param t: time to move
:param r: blend radius
'''
def move_joint_with_pose(pose: list=[0, 0, 0, 0, 0, 0], a: float=1.4, v: float=1.05, t: float=0, r: float=0):
    realtime.send(realtime_commands.move_joint_with_pose(pose, a, v, t, r))
    _wait_robot_move_done()

'''
move pose
:param pose: pose to move to
:param a: acceleration
:param v: velocity
:param t: time to move
:param r: blend radius
'''
def move_linear_pose(pose: list=[0, 0, 0, 0, 0, 0], a: float=1.4, v: float=1.05, t: float=0, r: float=0):
    realtime.send(realtime_commands.move_linear_pose(pose, a, v, t, r))
    _wait_robot_move_done()

'''
wait for robot to finish moving
'''
def _wait_robot_move_done():
    _robot_started_moving()
    _robot_done_moving()
'''
robot started moving
'''
def _robot_started_moving():
    while True:
        status = _get_program_state()
        if status != 1:
            break
        sleep(0.001)

'''
robot done moving
'''
def _robot_done_moving() -> bool:
    while True:
        status = _get_program_state()
        if status == 1:
            break
        sleep(0.001)

'''
get program state
:1 - normal
:2 - running
'''
def _get_program_state():
    # Receive responce
    responce = realtime.receive_status()

    # Unpack responce
    realtime_statuses.unpack(responce)

    # Get program state
    prgstate = realtime_statuses.get_program_state()
    return prgstate