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
    # Init UR Control
    ur_control.init('192.168.157.128')

    # Send power on command
    ur_control.power_on()

    # Send break release command
    ur_control.break_release()

    # Do pick and place
    PickAndPlace()
    

def PickAndPlace():
    # define positions
    p1_home = [0.380, -0.200, 0.500, 3, 0.1, 0.7]

    p2_pick = [0.580, -0.200, 0.500, 3, 0.1, 0.7]
    p2_offset_approach = [-0.200, 0.000, 0.000, 0, 0, 0]
    p2_offset_leave = [0.000, 0.000, 0.200, 0, 0, 0]

    p3_place = [0.580, -0.700, 0.500, 3, 0.1, 0.7]
    p3_offset_approach = [0.000, 0.000, 0.200, 0, 0, 0]
    p3_offset_leave = [-0.200, 0.000, 0.000, 0, 0, 0]

    # Pick 
    ur_control.move_joint_with_pose(p1_home, a=1.4, v=1.05, t=0, r=0) # move to p1_home
    ur_control.move_joint_with_pose(list(map(add,p2_pick,p2_offset_approach)), a=1.4, v=1.05, t=0, r=0) # move to p2_pick with offset for approach
    ur_control.move_linear_pose(p2_pick, a=1.4, v=1.05, t=0, r=0) # move to p2_pick with linear motion
    # pick the piece
    ur_control.move_joint_with_pose(list(map(add,p2_pick,p2_offset_leave)), a=1.4, v=1.05, t=0, r=0) # move to p2_pick with offset to leave

    # Place
    ur_control.move_joint_with_pose(list(map(add,p3_place,p3_offset_approach)), a=1.4, v=1.05, t=0, r=0) # move to p3_place with offset for approach
    ur_control.move_linear_pose(p3_place, a=1.4, v=1.05, t=0, r=0) # move to p3_place with linear motion
    # place the piece
    ur_control.move_joint_with_pose(list(map(add,p3_place,p3_offset_leave)), a=1.4, v=1.05, t=0, r=0) # move to p3_place with offset to leave


if __name__ == '__main__':
    program()
