import struct

'''
private properties
'''
_program_state : float = None
_robot_mode : float = None

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
    global _program_state, _robot_mode
    packlen = (struct.unpack('!i', data[0:4]))[0]
    if packlen == 1220: #for version 5.10 package
        data = data[4:]
        _program_state = (struct.unpack('!d', data[131*8:132*8]))[0]
    elif packlen == 1140: #for version 5.9 package
        data = data[4:]
        _program_state = (struct.unpack('!d', data[131*8:132*8]))[0]
        _robot_mode = (struct.unpack('!d', data[94*8:95*8]))[0]

def get_program_state():
    global _program_state
    return _program_state

def get_robot_mode():
    global _robot_mode
    return _robot_mode