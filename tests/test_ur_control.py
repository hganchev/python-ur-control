import unittest
from unittest import mock
from pyURControl import ur_control

class TestURControl(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)

    def setUp(self) -> None:
        pass

    def test_power_on(self):
        # arrange
        #!TDB

        # act

        # assert
        self.assertEqual(True, True)

    def test_create_pallet(self):
        # arrange
        rows = 3
        cols = 3
        corner1 = [0.5, 0.5, 0.5, 0, 0, 0]
        corner2 = [0.5, 0.5, 0.5, 0, 0, 0]
        corner3 = [0.5, 0.5, 0.5, 0, 0, 0]

        # act
        pallet = ur_control.create_pallet(rows, cols, corner1, corner2, corner3)

        # assert
        self.assertEqual(len(pallet), rows * cols)

    def test_go_to_pallet_position(self):
        # arrange
        rows = 3
        cols = 3
        corner1 = [0.5, 0.5, 0.5, 0, 0, 0]
        corner2 = [0.5, 0.5, 0.5, 0, 0, 0]
        corner3 = [0.5, 0.5, 0.5, 0, 0, 0]
        pallet = ur_control.create_pallet(rows, cols, corner1, corner2, corner3)
        row = 0
        col = 0

        # act
        ur_control.go_to_pallet_position(pallet, row, col)

        # assert
        self.assertEqual(True, True)

    def test_go_to_pallet_position_with_offset(self):
        # arrange
        rows = 3
        cols = 3
        corner1 = [0.5, 0.5, 0.5, 0, 0, 0]
        corner2 = [0.5, 0.5, 0.5, 0, 0, 0]
        corner3 = [0.5, 0.5, 0.5, 0, 0, 0]
        pallet = ur_control.create_pallet(rows, cols, corner1, corner2, corner3)
        row = 1
        col = 1
        offset = [0.1, 0.1, 0.1, 0, 0, 0]

        # act
        ur_control.go_to_pallet_position_with_offset(pallet, row, col, offset)

        # assert
        self.assertEqual(True, True)

    def test_create_pallet(self):
        # arrange
        rows = 3
        cols = 3
        corner1 = [0.5, 0.5, 0.5, 0, 0, 0]
        corner2 = [0.6, 0.5, 0.5, 0, 0, 0]
        corner3 = [0.5, 0.6, 0.5, 0, 0, 0]

        # act
        pallet = ur_control.create_pallet(rows, cols, corner1, corner2, corner3)

        # assert
        self.assertEqual(len(pallet), rows * cols)
        self.assertEqual(pallet[0], [0.5, 0.5, 0.5, 0, 0, 0])
        self.assertEqual(pallet[1], [0.55, 0.5, 0.5, 0, 0, 0])
        self.assertEqual(pallet[2], [0.6, 0.5, 0.5, 0, 0, 0])
        self.assertEqual(pallet[3], [0.5, 0.55, 0.5, 0, 0, 0])
        self.assertEqual(pallet[4], [0.55, 0.55, 0.5, 0, 0, 0])
        self.assertEqual(pallet[5], [0.6, 0.55, 0.5, 0, 0, 0])
        self.assertEqual(pallet[6], [0.5, 0.6, 0.5, 0, 0, 0])
        self.assertEqual(pallet[7], [0.55, 0.6, 0.5, 0, 0, 0])
        self.assertEqual(pallet[8], [0.6, 0.6, 0.5, 0, 0, 0])

    def test_go_to_pallet_position(self):
        # arrange
        rows = 3
        cols = 3
        corner1 = [0.5, 0.5, 0.5, 0, 0, 0]
        corner2 = [0.6, 0.5, 0.5, 0, 0, 0]
        corner3 = [0.5, 0.6, 0.5, 0, 0, 0]
        pallet = ur_control.create_pallet(rows, cols, corner1, corner2, corner3)
        row = 1
        col = 1

        # act
        ur_control.go_to_pallet_position(pallet, row, col)

        # assert
        self.assertEqual(True, True)

    def test_go_to_pallet_position_with_offset(self):
        # arrange
        rows = 3
        cols = 3
        corner1 = [0.5, 0.5, 0.5, 0, 0, 0]
        corner2 = [0.6, 0.5, 0.5, 0, 0, 0]
        corner3 = [0.5, 0.6, 0.5, 0, 0, 0]
        pallet = ur_control.create_pallet(rows, cols, corner1, corner2, corner3)
        row = 1
        col = 1
        offset = [0.1, 0.1, 0.1, 0, 0, 0]

        # act
        ur_control.go_to_pallet_position_with_offset(pallet, row, col, offset)

        # assert
        self.assertEqual(True, True)
