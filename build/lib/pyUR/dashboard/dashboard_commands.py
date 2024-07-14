'''
This file contains all the commands that can be sent to the robot dashboard (port 29999) server.
'''

def __init__():
    pass

def load_program(program:str='MainProgram.urp') -> str:
    '''
    command for loading program to robot controller
    :param program: program name - MainProgram.urp
    '''
    return "load " + program + '\n'

def load_installation(installation:str='default.installation') -> str:
    '''
    command for loading program to robot controller
    :param installation: installation name - default.installation
    '''
    return "load installation " + installation + '\n'

def play_program() -> str:
    '''
    command for playing program
    '''
    return "play" + '\n'

def stop_program() -> str:
    '''
    command for stopping program
    '''
    return "stop" + '\n'

def pause_program() -> str:
    '''
    command for pausing program
    '''
    return "pause" + '\n'

def quit_program() -> str:
    '''
    command for quitting program
    '''
    return "quit" + '\n'

def shutdown() -> str:
    '''
    command for shutting down robot
    '''
    return "shutdown" + '\n'

def running() -> str:
    '''
    command for getting running status of robot
    '''
    return "running" + '\n'

def program_state() -> str:
    '''
    command for getting program state of robot
    '''
    return "programState" + '\n'

def power_on() -> str:
    '''
    command for powering on robot
    '''
    return "power on" + '\n'

def power_off() -> str:
    '''
    command for powering off robot
    '''
    return "power off" + '\n'

def brake_release() -> str:
    '''
    command for releasing brake
    '''
    return "brake release" + '\n'

def unlock_protective_stop() -> str:
    '''
    command for unlocking protective stop
    '''
    return "unlock protective stop" + '\n'

def safety_status() -> str:
    '''
    command for getting safety status of robot
    '''
    return "safetystatus" + '\n'

def robotmode() -> str:
    '''
    command for getting robot mode
    '''
    return "robotmode" + '\n'

def is_in_remote_control() -> str:
    '''
    command for checking if robot is in remote control
    '''
    return "is in remote control" + '\n'
