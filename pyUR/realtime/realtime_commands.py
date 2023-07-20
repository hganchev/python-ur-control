class realtime_commands:
    def __init__(self):
        pass

    '''
    set TCP of robot
    :param tcp: tcp position - [x, y, z, rx, ry, rz]
    '''
    def set_tcp(self, tcp:list=[0, 0, 0, 0, 0, 0]) -> str:
        return "set_tcp(" + str(tcp) + ")" + '\n'

    '''
    send move joint to robot
    :param joint: joint position - [base, shoulder, elbow, wrist 1, wrist 2, wrist 3]
    :param a: acceleration - 1.4
    :param v: velocity - 1.05
    :param t: time - 0
    '''
    def move_joint(self, joint:list=[0, 0, 0, 0, 0, 0], a:float=1.4, v:float=1.05, t:float=0) -> str:
        return "movej(" + str(joint) + ", a=" + str(a) + ", v=" + str(v) + ", t=" + str(t) + ")" + '\n'
    
    '''
    send move pose to robot
    :param pose: pose position - [x, y, z, rx, ry, rz]
    :param a: acceleration - 1.4
    :param v: velocity - 1.05
    :param t: time - 0
    '''
    def move_pose(self, pose:list=[0, 0, 0, 0, 0, 0], a:float=1.4, v:float=1.05, t:float=0) -> str:
        return "movel(" + str(pose) + ", a=" + str(a) + ", v=" + str(v) + ", t=" + str(t) + ")" + '\n'

    '''
    calculate inverse kinematics of robot pose
    :param pose: pose position - [x, y, z, rx, ry, rz]
    '''
    def inverse_kinematics(self, pose:list=[0, 0, 0, 0, 0, 0]) -> str:
        return "get_inverse_kin(" + str(pose) + ")" + '\n'
    
    '''
    calculate forward kinematics of robot joint
    :param joint: joint position - [base, shoulder, elbow, wrist 1, wrist 2, wrist 3]
    '''
    def forward_kinematics(self, joint:list=[0, 0, 0, 0, 0, 0]) -> str:
        return "get_forward_kin(" + str(joint) + ")" + '\n'
    