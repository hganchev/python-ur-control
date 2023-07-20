import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
from pyURControl import ur_control
from time import sleep
import asyncio

'''
make your program here
'''
async def program():
    # Init UR Control
    ur_control.init('192.168.157.128')

    # Send power on command
    ur_control.power_on()

    # Send break release command
    ur_control.break_release()

    # Send move joint with pose command
    await ur_control.move_joint_with_pose([0.380, -0.200, 0.500, 3, 0.1, 0.7])


if __name__ == '__main__':
    asyncio.run(program())

