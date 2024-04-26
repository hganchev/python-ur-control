'''
This file contains the commands that can be sent to the robot.
'''
def __init__():
    pass

def set_tcp(tcp:list=[0, 0, 0, 0, 0, 0]) -> str:
    '''
    set TCP of robot
    :param tcp: tcp position - [x, y, z, rx, ry, rz]
    '''
    return "set_tcp(p" + str(tcp) + ")" + '\n'

def set_target_payload(payload:float=0, cog:list=[0, 0, 0], inertia:list=[0,0,0,0,0,0]) -> str:
    '''
    set payload of robot
    :param payload: payload in kg
    :param cog: center of gravity - [CoGx, CoGy, CoGz]
    :param inertia: inertia - [Ixx, Ixy, Ixz, Iyy, Iyz, Izz]
    '''
    return "set_target_payload(" + str(payload) + ", p" + str(cog) + "," + str(inertia) + ")" + '\n'

def move_joint(joint:list=[0, 0, 0, 0, 0, 0], a:float=1.4, v:float=1.05, t:float=0, r:float=0) -> str:
    '''
    send move joint to robot
    :param joint: joint position - [base, shoulder, elbow, wrist 1, wrist 2, wrist 3] in radians
    :param a: acceleration - 1.4
    :param v: velocity - 1.05
    :param t: time - 0
    :param r: radius - 0
    '''
    return "movej(" + str(joint) + ", a=" + str(a) + ", v=" + str(v) + ", t=" + str(t) + ", r=" + str(r) + ")" + '\n'

def move_joint_with_pose(pose:list=[0, 0, 0, 0, 0, 0], a:float=1.4, v:float=1.05, t:float=0, r:float=0) -> str:
    '''
    send move joint with pose to robot
    :param pose: pose position - [x, y, z, rx, ry, rz]
    :param a: acceleration - 1.4
    :param v: velocity - 1.05
    :param t: time - 0
    :param r: radius - 0
    '''
    return "movej(" + inverse_kinematics(pose) + ", a=" + str(a) + ", v=" + str(v) + ", t=" + str(t) + ", r=" + str(r) + ")" + '\n'

def move_linear_pose(pose:list=[0, 0, 0, 0, 0, 0], a:float=1.4, v:float=1.05, t:float=0, r:float=0) -> str:
    '''
    send move pose to robot
    :param pose: pose position - [x, y, z, rx, ry, rz]
    :param a: acceleration - 1.4
    :param v: velocity - 1.05
    :param t: time - 0
    :param r: radius - 0
    '''
    return "movel(p" + str(pose) + ", a=" + str(a) + ", v=" + str(v) + ", t=" + str(t) + ", r=" + str(r) + ")" + '\n'

def inverse_kinematics(pose:list=[0, 0, 0, 0, 0, 0]) -> str:
    '''
    calculate inverse kinematics of robot pose
    :param pose: pose position - [x, y, z, rx, ry, rz]
    '''
    return "get_inverse_kin(p" + str(pose) + ")"

def forward_kinematics(joint:list=[0, 0, 0, 0, 0, 0]) -> str:
    '''
    calculate forward kinematics of robot joint
    :param joint: joint position - [base, shoulder, elbow, wrist 1, wrist 2, wrist 3]
    '''
    return "get_forward_kin(" + str(joint) + ")"

def pose_add(pose1:list=[0, 0, 0, 0, 0, 0], pose2:list=[0, 0, 0, 0, 0, 0]) -> str:
    '''
    calculate add two poses
    :param pose1: pose position - [x, y, z, rx, ry, rz]
    :param pose2: pose position - [x, y, z, rx, ry, rz]
    '''
    return "pose_add(p" + str(pose1) + ", p" + str(pose2) + ")"

def pose_translate(pose1:list=[0, 0, 0, 0, 0, 0], pose2:list=[0, 0, 0, 0, 0, 0]) -> str:
    '''
    calculate translation of two poses
    :param pose1: pose position - [x, y, z, rx, ry, rz]
    :param pose2: pose position - [x, y, z, rx, ry, rz]
    '''
    return "pose_trans(p" + str(pose1) + ", p" + str(pose2) + ")"


def pose_inverse(pose:list=[0, 0, 0, 0, 0, 0]) -> str:
    '''
    inverse pose 
    :param pose: pose position - [x, y, z, rx, ry, rz]
    '''
    return "pose_inv(p" + str(pose) + ")"


def pose_sub(pose1:list=[0, 0, 0, 0, 0, 0], pose2:list=[0, 0, 0, 0, 0, 0]) -> str:
    '''
    calculate sub pose of two poses
    :param pose1: pose position - [x, y, z, rx, ry, rz]
    :param pose2: pose position - [x, y, z, rx, ry, rz]
    '''
    return "pose_sub(p" + str(pose1) + ", p" + str(pose2) + ")"


def set_digital_output(output:int=0, value:bool=False) -> str:
    '''
    set digital output
    :param output: output number - 0-7
    '''
    return "set_standard_digital_out(" + str(output) + ", " + str(value) +")" + '\n'
