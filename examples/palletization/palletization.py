from pyURControl import ur_control
from time import sleep
from operator import add

'''
make your program here
to Install pyURControl localy, run the following command: pip install -e .
'''
def program():
    # Init UR Control
    ur_control.init('192.168.1.28')

    # Send power on command
    ur_control.power_on()

    # Send break release command
    ur_control.break_release()

    # Do palletization pick
    Palletization()

    

def Palletization():
    # Create a pallet
    corner1 = [0.300, -0.500, 0.275, 3.1, -0.018, 0.115]
    corner2 = [0.300, -0.750, 0.275, 3.1, -0.018, 0.115]
    corner3 = [0.600, -0.500, 0.275, 3.1, -0.018, 0.115]
    pallet1 = ur_control.create_pallet(rows=10, cols=10, corner1=corner1, corner2=corner2, corner3=corner3)

    # set tcp
    ur_control.set_tcp([0, 0, 0.2, 0, 0, 0])

    # set payload if there is any
    ur_control.set_payload(0, [0, 0, 0], [0,0,0,0,0,0])

    # move to pallet position 1
    ur_control.go_to_pallet_position(pallet1, 1)

    # move to pallet position 2
    ur_control.go_to_pallet_position(pallet1, 2)

    # move to pallet position 2
    ur_control.go_to_pallet_position(pallet1, 100)


if __name__ == '__main__':
    program()

