## UR control
Contains 1 class:
- ur_control.py - wrapper class that contains functions to be used for 
controlling the robot behavior.

## Functions
- init(ip) - initializes the robot connection
- power_on() - powers on the robot
- brake_release() - releases the robot brakes
- set_tcp(tcp) - sets the tool center point
- set_payload(mass, cog, inertia) - sets the payload
- move_joint_with_pose(joints, a=1.4, v=1.05) - moves the robot to the specified joint position
- move_linear_pose(pose, a=1.2, v=0.25) - moves the robot to the specified pose

## Implementation
```python
from pyURControl import ur_control
```

## Usage
```python
ur_control.init("ROBOT_IP")
```