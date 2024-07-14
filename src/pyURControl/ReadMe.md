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
- create_pallet(rows, cols, corner1, corner2, corner3) - creates a pallet with the specified rows, columns, and corner points
- go_to_pallet_position(pallet, row, col, a=1.4, v=1.05, t=0, r=0) - moves the robot to the specified pallet position
- go_to_pallet_position_with_offset(pallet, row, col, offset, a=1.4, v=1.05, t=0, r=0) - moves the robot to the specified pallet position with an offset

## Implementation
```python
from pyURControl import ur_control
```

## Usage
```python
ur_control.init("ROBOT_IP")
pallet = ur_control.create_pallet(3, 3, [0.5, 0.5, 0.5, 0, 0, 0], [0.5, 0.5, 0.5, 0, 0, 0], [0.5, 0.5, 0.5, 0, 0, 0])
ur_control.go_to_pallet_position(pallet, 0, 0)
ur_control.go_to_pallet_position_with_offset(pallet, 1, 1, [0.1, 0.1, 0.1, 0, 0, 0])
```
