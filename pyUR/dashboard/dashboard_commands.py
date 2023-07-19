class dashboard_commands:
    def __init__(self):
        pass
    
    '''
    command for loading program to robot controller
    :param program: program name - MainProgram.urp
    '''
    def load_program(self, program:str='MainProgram.urp') -> str:
        return "load " + program + '\n'
    
    '''
    command for loading program to robot controller
    :param installation: installation name - default.installation
    '''
    def load_installation(self, installation:str='default.installation') -> str:
        return "load installation " + installation + '\n'
    
    '''
    command for playing program
    '''
    def play_program(self) -> str:
        return "play" + '\n'
    
    '''
    command for stopping program
    '''
    def stop_program(self) -> str:
        return "stop" + '\n'
    
    '''
    command for pausing program
    '''
    def pause_program(self) -> str:
        return "pause" + '\n'
    
    '''
    command for quitting program
    '''
    def quit_program(self) -> str:
        return "quit" + '\n'
    
    '''
    command for shutting down robot
    '''
    def shutdown(self) -> str:
        return "shutdown" + '\n'
    
    '''
    command for getting running status of robot
    '''
    def running(self) -> str:
        return "running" + '\n'
    
    '''
    command for getting program state of robot
    '''
    def program_state(self) -> str:
        return "programState" + '\n'
    
    '''
    command for powering on robot
    '''
    def power_on(self) -> str:
        return "power on" + '\n'
    
    '''
    command for powering off robot
    '''
    def power_off(self) -> str:
        return "power off" + '\n'
    
    '''
    command for releasing brake
    '''
    def brake_release(self) -> str:
        return "brake release" + '\n'
    
    '''
    command for unlocking protective stop
    '''
    def unlock_protective_stop(self) -> str:
        return "unlock protective stop" + '\n'
    
    '''
    command for getting safety status of robot
    '''
    def safety_status(self) -> str:
        return "safetystatus" + '\n'
    
    '''
    command for getting robot mode
    '''
    def robotmode(self) -> str:
        return "robotmode" + '\n'
    
    '''
    command for checking if robot is in remote control
    '''
    def is_in_remote_control(self) -> str:
        return "is in remote control" + '\n'

    '''
    function for parsing status of the robot
    '''
    def parse_status(self, received :str) -> str:
        return None