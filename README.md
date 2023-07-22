# python-ur-control
This is package for basic control of Universal Robots using inbuild intefaces
like Dashboard, Realtime, RTDE.

## Dashboard 
Dashboard is a tcp/ip socket communication to port 29999 with functionalities like:
- Loading program and installation to robot
- Enabling the robot (Servo on/off, Break release)
- Control of the program (Play, Stop, Pause)

## Realtime interface
Realtime interface is a tcp/ip socket communication to port 30003 with functionalities like:
- movej - joint movements
- movel - linear movements
- digital io control (gripper control)
- robot statuses (program state, robot state, actual pose etc.)

It is using UR Script commands for controling the robot behavior. 

## RTDE - tbd?
