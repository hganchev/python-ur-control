import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
from pyUR.dashboard import dashboard, dashboard_commands
from pyUR.realtime import realtime, realtime_commands, realtime_statuses
from time import sleep

def __init__():
   pass

def init(host_ip: str='127.0.0.1'):
    '''
    init dashboard server and realtime server
    :param host_ip: host ip address
    '''
    # create a dashboard object
    dashboard.init_socket(host_ip=host_ip)
    if dashboard.is_connected():
        print('Connected to UR Dashboard Server')

    # create a realtime object
    realtime.init_socket(host_ip=host_ip)

def power_on():
    '''
    send power on command
    '''
    responce = dashboard.send_receive_socket(dashboard_commands.power_on())
    print(responce)
    if 'Powering on' in responce:
        _wait_robot_powered_on()

def _wait_robot_powered_on():
    '''
    wait for robot to be powered on
    '''
    while True:
        responce = dashboard.send_receive_socket(dashboard_commands.robotmode())
        if 'Robotmode: IDLE' in responce or \
        'Robotmode: RUNNING' in responce:
            break
        sleep(0.001)

def break_release():
    '''
    send brake release command
    '''
    responce = dashboard.send_receive_socket(dashboard_commands.brake_release())
    print(responce)
    if 'Brake releasing' in responce:
        _wait_robot_break_released()

def _wait_robot_break_released():
    '''
    wait for robot break realeased
    '''
    while True:
        responce = dashboard.send_receive_socket(dashboard_commands.robotmode())
        if 'Robotmode: RUNNING' in responce:
            break
        sleep(0.001)


def set_tcp(tcp_offset: list=[0, 0, 0, 0, 0, 0], delay: float=0.3):
    '''
    set tcp
    :param tcp_offset: tcp offset
    :param delay: delay for command to be executed 0.3s by default
    '''
    realtime.send(realtime_commands.set_tcp(tcp_offset))
    sleep(delay) # set sleep for command to be executed

def set_payload(payload: float=0, cog: list=[0, 0, 0], inertia: list=[0,0,0,0,0,0]):
    '''
    set payload
    :param payload: payload in kg
    :param cog: center of gravity [CoGx, CoGy, CoGz] specifying the offset (in meters) from the tool mount.
    :param inertia: inertia [Ixx, Ixy, Ixz, Iyy, Iyz, Izz]  - in kg*m^2 !can not be negative!
    '''
    realtime.send(realtime_commands.set_target_payload(payload, cog, inertia))

def move_joint_with_pose(pose: list=[0, 0, 0, 0, 0, 0], a: float=1.4, v: float=1.05, t: float=0, r: float=0):
    '''
    move joint with pose
    :param pose: pose to move to
    :param a: acceleration
    :param v: velocity
    :param t: time to move
    :param r: blend radius
    '''
    realtime.send(realtime_commands.move_joint_with_pose(pose, a, v, t, r))
    _wait_robot_move_done()

def move_linear_pose(pose: list=[0, 0, 0, 0, 0, 0], a: float=1.4, v: float=1.05, t: float=0, r: float=0):
    '''
    move pose
    :param pose: pose to move to
    :param a: acceleration
    :param v: velocity
    :param t: time to move
    :param r: blend radius
    '''
    realtime.send(realtime_commands.move_linear_pose(pose, a, v, t, r))
    _wait_robot_move_done()

def _get_program_state() -> float:
    '''
    get program state
    :0 - ?
    :1 - normal
    :2 - running
    '''
    # Receive responce
    responce = realtime.receive_status()

    # Unpack responce
    realtime_statuses.unpack(responce)

    # Get program state
    prgstate = realtime_statuses.get_program_state()
    return prgstate

def _robot_started_moving():
    '''
    robot started moving
    '''
    while True:
        status = _get_program_state()
        if status != 1:
            break
        sleep(0.001)

def _robot_done_moving() -> bool:
    '''
    robot done moving
    '''
    while True:
        status = _get_program_state()
        if status == 1:
            break
        sleep(0.001)

def _wait_robot_move_done():
    '''
    wait for robot to finish moving
    '''
    _robot_started_moving()
    _robot_done_moving()

def set_digital_output(output: int=0, value: bool=False):
    '''
    set digital output
    :param output: output number 0-7
    :param value: output value
    '''
    realtime.send(realtime_commands.set_digital_output(output, value))
    _wait_digital_output_is_set(output, value)

def get_digital_outputs() -> list:
    '''
    get digital outputs
    '''
    # Receive responce
    responce = realtime.receive_status()

    # Unpack responce
    realtime_statuses.unpack(responce)

    # Get program state
    digital_outputs = realtime_statuses.get_digital_outputs()
    return digital_outputs

def _wait_digital_output_is_set(output: int=0, value: bool=False):
    '''
    wait for digital output to be set
    :param output: output number 0-7
    :param value: output value
    '''
    while True:
        digital_outputs = get_digital_outputs()
        if digital_outputs[output] == value:
            break
        sleep(0.001)

def get_digital_inputs() -> list:
    '''
    get digital inputs
    '''
    # Receive responce
    responce = realtime.receive_status()

    # Unpack responce
    realtime_statuses.unpack(responce)

    # Get program state
    digital_inputs = realtime_statuses.get_digital_inputs()
    return digital_inputs

def get_digital_input(input: int=0) -> bool:
    '''
    get digital input
    :param input: input number 0-7
    '''
    # Receive responce
    responce = realtime.receive_status()

    # Unpack responce
    realtime_statuses.unpack(responce)
    
    digital_inputs = get_digital_inputs()
    return digital_inputs[input]