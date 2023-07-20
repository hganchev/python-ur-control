import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
from pyUR.dashboard import dashboard, dashboard_commands
from pyUR.realtime import realtime, realtime_commands, realtime_statuses
from time import sleep
import asyncio

# create a dashboard object
dashboard.init_socket(host_ip='192.168.157.128')
if dashboard.is_connected():
    print('Connected to UR Dashboard Server')

# create a realtime object
realtime.init_socket('192.168.157.128')

'''
make your program here
'''
async def control(queue):
    # Send power on command
    responce = dashboard.send_receive_socket(dashboard_commands.power_on())
    print(responce)

    # Send break release command
    responce = dashboard.send_receive_socket(dashboard_commands.brake_release())
    print(responce)

    # Send move joint with pose command
    realtime.send(realtime_commands.move_joint_with_pose([0.380, -0.200, 0.500, 3, 0.1, 0.7]))
    print('Waiting for robot to start moving')
    while True:
        status = await queue.get()
        if status != 1:
            break
        await asyncio.sleep(0.001)

    print('Robot started moving')
    while True:
        status = await queue.get()
        if status == 1:
            break
        await asyncio.sleep(0.001)
    print('Robot done moving')

'''
get realtime status values
'''
async def get_realtime_status(queue):
    last_prgstate = 0
    last_rbtmode = 0

    while True:
        # Send get robot status command
        responce = realtime.receive_status()
        realtime_statuses.unpack(responce)
        prgstate = realtime_statuses.get_program_state()
        rbtmode = realtime_statuses.get_robot_mode()

        if prgstate != last_prgstate:
            last_prgstate = prgstate
            print('prg state:' + str(prgstate))
        if rbtmode != last_rbtmode:
            last_rbtmode = rbtmode
            print('rbt mode:' + str(rbtmode))
            
        await queue.put(prgstate)
        await asyncio.sleep(1/500) # 500Hz = 1/500 = 0.002s = 2ms
        

''' 
main function
'''
async def main():
    # Create a queue that we will use to store our "workload".
    queue = asyncio.Queue()

    # Create tasks for both functions to run concurrently
    task1 = asyncio.create_task(control(queue))
    task2 = asyncio.create_task(get_realtime_status(queue))

    # Wait for both tasks to complete
    await task1
    await task2


if __name__ == '__main__':
    asyncio.run(main())

