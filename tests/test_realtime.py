import unittest
from unittest import mock
from pyUR.realtime import realtime, realtime_commands, realtime_statuses
import struct

class TestRealtime(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)

    def setUp(self) -> None:
        pass
          
    def test_realtime_init(self):
        # arrange
        realtime.init_socket("192.168.157.128")

        # act

        # assert
        self.assertEqual(True, True)

    def test_double_to_8bit_list(self):
        # arrange
        value = 16.0

        # act
        actual = realtime_statuses._double_to_8bit_list(value)
        expected = [False, False, False, False, True, False, False, False]

        # assert
        self.assertEqual(actual, expected)

    def test_unpack_program_state(self):
        # arrange
        responce = bytearray(1140)
        responce[0:4] = struct.pack('!i', 1140)
        
        value = 1.0
        struct.pack_into("!d", responce, 131*8 + 4, value)
        print(struct.unpack('!d', responce[4:][131*8:132*8])[0])

        program_states = [0, 1, 2] # 0 - ?, 1 - Normal, 2 - running

        # act
        realtime_statuses.unpack(responce)
        actual = realtime_statuses.get_program_state()
        expected = program_states[1]

        # assert
        self.assertEqual(actual, expected)

    def test_unpack_digital_outputs(self):
        # arrange
        responce = bytearray(1140)
        responce[0:4] = struct.pack('!i', 1140)

        value = 16.0
        struct.pack_into("!d", responce, 130*8 + 4, value)

        print(struct.unpack('!d', responce[4:][130*8:131*8]))
        # act
        realtime_statuses.unpack(responce)
        actual = realtime_statuses.get_digital_outputs()
        expected = [False, False, False, False, True, False, False, False]

        # assert
        self.assertEqual(actual, expected)