import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
from pyUR.dashboard import dashboard, dashboard_commands
from pyUR.realtime import realtime, realtime_commands, realtime_statuses
from time import sleep
import asyncio

'''
inut ur control by creating a thread
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
move joint with pose
'''
async def move_joint_with_pose(pose: list=[0, 0, 0, 0, 0, 0]):
    realtime.send(realtime_commands.move_joint_with_pose(pose))
    await robot_started_moving() == True 
    await robot_done_moving() == True

'''
move pose
'''
async def move_pose(pose: list=[0, 0, 0, 0, 0, 0]):
    realtime.send(realtime_commands.move_pose(pose))
    await robot_started_moving() == True 
    await robot_done_moving() == True
    
'''
robot started moving
'''
async def robot_started_moving() -> bool:
    while True:
        status = await get_program_state()
        if status != 1:
            break
        await asyncio.sleep(0.001)
    return True

'''
robot done moving
'''
async def robot_done_moving() -> bool:
    while True:
        status = await get_program_state()
        if status == 1:
            break
        await asyncio.sleep(0.001)
    return True

'''
get program state
'''
async def get_program_state():
    # Send get robot status command
    responce = realtime.receive_status()

    # Unpack responce
    realtime_statuses.unpack(responce)

    # Get program state
    prgstate = realtime_statuses.get_program_state()
    rbtmode = realtime_statuses.get_robot_mode()

    return prgstate