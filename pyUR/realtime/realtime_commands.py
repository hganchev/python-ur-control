'''
This file contains the commands that can be sent to the robot.
'''
def __init__():
    pass

'''
set TCP of robot
:param tcp: tcp position - [x, y, z, rx, ry, rz]
'''
def set_tcp(tcp:list=[0, 0, 0, 0, 0, 0]) -> str:
    return "set_tcp(p" + str(tcp) + ")" + '\n'

'''
send move joint to robot
:param joint: joint position - [base, shoulder, elbow, wrist 1, wrist 2, wrist 3]
:param a: acceleration - 1.4
:param v: velocity - 1.05
:param t: time - 0
:param r: radius - 0
'''
def move_joint(joint:list=[0, 0, 0, 0, 0, 0], a:float=1.4, v:float=1.05, t:float=0, r:float=0) -> str:
    return "movej(" + str(joint) + ", a=" + str(a) + ", v=" + str(v) + ", t=" + str(t) + ", r=" + str(r) + ")" + '\n'


'''
send move joint with pose to robot
:param pose: pose position - [x, y, z, rx, ry, rz]
:param a: acceleration - 1.4
:param v: velocity - 1.05
:param t: time - 0
:param r: radius - 0
'''
def move_joint_with_pose(pose:list=[0, 0, 0, 0, 0, 0], a:float=1.4, v:float=1.05, t:float=0, r:float=0) -> str:
    return "movej(" + inverse_kinematics(pose) + ", a=" + str(a) + ", v=" + str(v) + ", t=" + str(t) + ", r=" + str(r) + ")" + '\n'

'''
send move pose to robot
:param pose: pose position - [x, y, z, rx, ry, rz]
:param a: acceleration - 1.4
:param v: velocity - 1.05
:param t: time - 0
:param r: radius - 0
'''
def move_linear_pose(pose:list=[0, 0, 0, 0, 0, 0], a:float=1.4, v:float=1.05, t:float=0, r:float=0) -> str:
    return "movel(p" + str(pose) + ", a=" + str(a) + ", v=" + str(v) + ", t=" + str(t) + ", r=" + str(r) + ")" + '\n'

'''
calculate inverse kinematics of robot pose
:param pose: pose position - [x, y, z, rx, ry, rz]
'''
def inverse_kinematics(pose:list=[0, 0, 0, 0, 0, 0]) -> str:
    return "get_inverse_kin(p" + str(pose) + ")"

'''
calculate forward kinematics of robot joint
:param joint: joint position - [base, shoulder, elbow, wrist 1, wrist 2, wrist 3]
'''
def forward_kinematics(joint:list=[0, 0, 0, 0, 0, 0]) -> str:
    return "get_forward_kin(" + str(joint) + ")"

'''
calculate add two poses
:param pose1: pose position - [x, y, z, rx, ry, rz]
:param pose2: pose position - [x, y, z, rx, ry, rz]
'''
def pose_add(pose1:list=[0, 0, 0, 0, 0, 0], pose2:list=[0, 0, 0, 0, 0, 0]) -> str:
    return "pose_add(p" + str(pose1) + ", p" + str(pose2) + ")"

'''
calculate translation of two poses
:param pose1: pose position - [x, y, z, rx, ry, rz]
:param pose2: pose position - [x, y, z, rx, ry, rz]
'''
def pose_translate(pose1:list=[0, 0, 0, 0, 0, 0], pose2:list=[0, 0, 0, 0, 0, 0]) -> str:
    return "pose_trans(p" + str(pose1) + ", p" + str(pose2) + ")"
