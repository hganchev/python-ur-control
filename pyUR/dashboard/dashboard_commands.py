class dashboard_commands:
    program = 'MainProgram.urp'
    installation = 'default.installation'
        
    '''
    commands for the dashboard server
    :keys: command, value: command string
    - load_program: load program to robot controller [program]
    - load_installation: load installation to robot controller [installation]
    '''
    commands = {
        "load_program": "load " + program,
        "load_installation": "load installation " + installation,
        "play_program": "play",
        "stop_program": "stop",
        "pause_program": "pause",
        "quit_program": "quit",
        "shutdown": "shutdown",
        "running": "running",
        "program_state": "programState",
        "power_on": "power on",
        "power_off": "power off",
        "brake_release": "brake release",
        "unlock_protective_stop": "unlock protective stop",
        "safety_status": "safetystatus",
        "robotmode": "robotmode",
        "is_in_remote_control": "is in remote control",
    }

    status = {
        "online": False,
        "booting": False,
        "powering_on": False,
        "break_released": False,
        "robot_is_ready": False,
        "program_loaded": False,
        "program_playing": False,
        "program_paused": False,
        "program_stopped": False,
    } 

    '''
    function for parsing status of the robot
    '''
    def parse_status(self) -> dict:
        global status
        status = status.decode("utf-8").split(" ")
        status_dict = {}
        for i in range(0, len(status), 2):
            status_dict[status[i]] = status[i+1]
        return status_dict