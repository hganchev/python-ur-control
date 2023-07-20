'''
This file contains all the commands that can be sent to the robot dashboard (port 29999) server.
'''

def __init__():
    pass

'''
command for loading program to robot controller
:param program: program name - MainProgram.urp
'''
def load_program(program:str='MainProgram.urp') -> str:
    return "load " + program + '\n'

'''
command for loading program to robot controller
:param installation: installation name - default.installation
'''
def load_installation(installation:str='default.installation') -> str:
    return "load installation " + installation + '\n'

'''
command for playing program
'''
def play_program() -> str:
    return "play" + '\n'

'''
command for stopping program
'''
def stop_program() -> str:
    return "stop" + '\n'

'''
command for pausing program
'''
def pause_program() -> str:
    return "pause" + '\n'

'''
command for quitting program
'''
def quit_program() -> str:
    return "quit" + '\n'

'''
command for shutting down robot
'''
def shutdown() -> str:
    return "shutdown" + '\n'

'''
command for getting running status of robot
'''
def running() -> str:
    return "running" + '\n'

'''
command for getting program state of robot
'''
def program_state() -> str:
    return "programState" + '\n'

'''
command for powering on robot
'''
def power_on() -> str:
    return "power on" + '\n'

'''
command for powering off robot
'''
def power_off() -> str:
    return "power off" + '\n'

'''
command for releasing brake
'''
def brake_release() -> str:
    return "brake release" + '\n'

'''
command for unlocking protective stop
'''
def unlock_protective_stop() -> str:
    return "unlock protective stop" + '\n'

'''
command for getting safety status of robot
'''
def safety_status() -> str:
    return "safetystatus" + '\n'

'''
command for getting robot mode
'''
def robotmode() -> str:
    return "robotmode" + '\n'

'''
command for checking if robot is in remote control
'''
def is_in_remote_control() -> str:
    return "is in remote control" + '\n'
