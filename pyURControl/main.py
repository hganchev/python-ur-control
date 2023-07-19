import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
from pyUR.dashboard.dashboard import dashboard
from pyUR.dashboard.dashboard_commands import dashboard_commands
from time import sleep

# Create a dashboard object
dash = dashboard('192.168.157.128')
if dash.is_connected():
    print('Connected to UR Dashboard Server')

# Create a dashboard_commands object
dash_cmd = dashboard_commands()

# Send power on command
responce = dash.send_receive_socket(dash_cmd.power_on())
print(responce)

