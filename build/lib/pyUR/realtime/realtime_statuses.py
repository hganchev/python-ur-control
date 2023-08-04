import struct

'''
private properties
'''
_program_state : float = None
_robot_mode : float = None
_digital_outputs: list = None
_digital_inputs : list = None

_q_act_base:float = None
_q_act_shoulder:float = None
_q_act_elbow:float = None
_q_act_wrist1: float = None
_q_act_wrist2: float = None
_q_act_wrist3:float = None

_tool_act_x:float = None
_tool_act_y:float = None
_tool_act_z:float = None
_tool_act_rx:float = None
_tool_act_ry:float = None
_tool_act_rz:float = None


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
    global _program_state, _robot_mode,_digital_outputs,_digital_inputs,\
    _q_act_base,_q_act_shoulder,_q_act_elbow,_q_act_wrist1,_q_act_wrist2,_q_act_wrist3,\
    _tool_act_x,_tool_act_y,_tool_act_z,_tool_act_rx,_tool_act_ry,_tool_act_rz
    

    packlen = (struct.unpack('!i', data[0:4]))[0]
    if packlen == 1220: #for version 5.10 package
        data = data[4:]
        # program state
        _program_state = (struct.unpack('!d', data[131*8:132*8]))[0]

        # robot mode
        _robot_mode = (struct.unpack('!d', data[94*8:95*8]))[0]

        # digital inputs
        _digital_inputs = _double_to_8bit_list(struct.unpack('!d', data[85*8:86*8])[0])

        # digital outputs
        _digital_outputs = _double_to_8bit_list((struct.unpack('!d', data[130*8:131*8]))[0])
        
        # actual joint positions
        _q_act_base     = (struct.unpack('!d', data[31*8:32*8]))[0]
        _q_act_shoulder = (struct.unpack('!d', data[32*8:33*8]))[0]
        _q_act_elbow    = (struct.unpack('!d', data[33*8:34*8]))[0]
        _q_act_wrist1   = (struct.unpack('!d', data[34*8:35*8]))[0]
        _q_act_wrist2   = (struct.unpack('!d', data[35*8:36*8]))[0]
        _q_act_wrist3   = (struct.unpack('!d', data[36*8:37*8]))[0]

    elif packlen == 1140: #for version 5.9 package
        data = data[4:]

        # program state - 0 -? 1 - normal 2 - running
        _program_state = (struct.unpack('!d', data[131*8:132*8]))[0]

        # robot mode
        _robot_mode = (struct.unpack('!d', data[94*8:95*8]))[0]

        # digital inputs
        _digital_inputs = _double_to_8bit_list(struct.unpack('!d', data[85*8:86*8])[0])

        # digital outputs
        _digital_outputs = _double_to_8bit_list(struct.unpack('!d', data[130*8:131*8])[0])
        
         # actual joint positions
        _q_act_base     = (struct.unpack('!d', data[31*8:32*8]))[0]
        _q_act_shoulder = (struct.unpack('!d', data[32*8:33*8]))[0]
        _q_act_elbow    = (struct.unpack('!d', data[33*8:34*8]))[0]
        _q_act_wrist1   = (struct.unpack('!d', data[34*8:35*8]))[0]
        _q_act_wrist2   = (struct.unpack('!d', data[35*8:36*8]))[0]
        _q_act_wrist3   = (struct.unpack('!d', data[36*8:37*8]))[0]

        # actual robot position coordinates - x,y,z,rx,ry,rz
        _tool_act_x = (struct.unpack('!d', data[55*8:56*8]))[0]
        _tool_act_y = (struct.unpack('!d', data[56*8:57*8]))[0]
        _tool_act_z = (struct.unpack('!d', data[57*8:58*8]))[0]
        _tool_act_rx = (struct.unpack('!d', data[58*8:59*8]))[0]
        _tool_act_ry = (struct.unpack('!d', data[59*8:60*8]))[0]
        _tool_act_rz = (struct.unpack('!d', data[60*8:61*8]))[0]


def get_program_state():
    global _program_state
    return _program_state

def get_robot_mode():
    global _robot_mode
    return _robot_mode

def get_q_act_joint_positions():
    global _q_act_base, _q_act_shoulder, _q_act_elbow,_q_act_wrist1, _q_act_wrist2, _q_act_wrist3
    return list[_q_act_base, _q_act_shoulder, _q_act_elbow, _q_act_wrist1, _q_act_wrist2, _q_act_wrist3]

def get_digital_outputs():
    global _digital_outputs
    return _digital_outputs

def get_digital_inputs():
    global _digital_inputs
    return _digital_inputs

def get_robot_act_pose():
    global _tool_act_x, _tool_act_y, _tool_act_z, _tool_act_rx, _tool_act_ry, _tool_act_rz
    return list[_tool_act_x, _tool_act_y, _tool_act_z, _tool_act_rx, _tool_act_ry, _tool_act_rz]

def _double_to_8bit_list(d):
    # Convert the integer to its binary representation as a string
    binary_str = bin(int(d))[2:].zfill(8)

    #Convert the binary string to a list of 0 and 1 values
    binary_array = [bool(int(bit)) for bit in binary_str]

    return binary_array[::-1]