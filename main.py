import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
from pyURControl import ur_control
from time import sleep
from operator import add

'''
make your program here
'''
def program():
    p1 = [0.380, -0.200, 0.500, 3, 0.1, 0.7]
    p2 = [0.480, -0.200, 0.500, 3, 0.1, 0.7]
    p3 = [0.580, -0.200, 0.500, 3, 0.1, 0.7]

    p3_offset_approach = [0.000, 0.000, -0.200, 0, 0, 0]
    p3_offset_leave = [-0.200, 0.000, 0.000, 0, 0, 0]

    t1 = 1
    t2 = 1
    t3 = 1
    # Init UR Control
    ur_control.init('192.168.157.128')

    # Send power on command
    ur_control.power_on()

    # Send break release command
    ur_control.break_release()

    # Send move joint with pose command
    ur_control.move_joint_with_pose(p1, t=t1) # move to p1 for time t1
    ur_control.move_joint_with_pose(p2, t=t2) # move to p2 for time t2

    ur_control.move_joint_with_pose(list(map(add,p3,p3_offset_approach))) # move to p3 with offset for approach
    ur_control.move_linear_pose(p3) # move to p3 with linear motion
    ur_control.move_joint_with_pose(list(map(add,p3,p3_offset_leave))) # move to p3 with offset to leave


if __name__ == '__main__':
    program()

