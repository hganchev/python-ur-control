import struct

'''
private properties
'''
_program_state : float = None
_robot_mode : float = None

_q_act_x:float = None
_q_act_y:float = None
_q_act_z:float = None
_q_act_rx: float = None
_q_act_ry: float = None
_q_act_rz:float = None

'''
Class for unpacking status from robot
'''
def __init__():
    pass

'''
unpack status from robot
:param status: status to unpack
'''
def unpack(data:bytes):
    global _program_state, _robot_mode, _q_act_x,\
    _q_act_y,_q_act_x,_q_act_rx,_q_act_ry,_q_act_rz

    packlen = (struct.unpack('!i', data[0:4]))[0]
    if packlen == 1220: #for version 5.10 package
        data = data[4:]
        _program_state = (struct.unpack('!d', data[131*8:132*8]))[0]
    elif packlen == 1140: #for version 5.9 package
        data = data[4:]
        
        # actual positions
        _q_act_x = (struct.unpack('!d', data[31*8:32*8]))[0]
        _q_act_y = (struct.unpack('!d', data[32*8:33*8]))[0]
        _q_act_z = (struct.unpack('!d', data[33*8:34*8]))[0]
        _q_act_rx = (struct.unpack('!d', data[34*8:35*8]))[0]
        _q_act_ry = (struct.unpack('!d', data[35*8:36*8]))[0]
        _q_act_rz = (struct.unpack('!d', data[36*8:37*8]))[0]
        
        # program state
        _program_state = (struct.unpack('!d', data[131*8:132*8]))[0]

        # robot mode
        _robot_mode = (struct.unpack('!d', data[94*8:95*8]))[0]

def get_program_state():
    global _program_state
    return _program_state

def get_robot_mode():
    global _robot_mode
    return _robot_mode

def get_q_act_pose():
    global _q_act_x, _q_act_y, _q_act_z,\
    _q_act_rx, _q_act_ry, _q_act_rz
    return list[_q_act_x, _q_act_y, _q_act_z, _q_act_rx, _q_act_ry, _q_act_rz]