import unittest
from unittest import mock
from pyUR.dashboard import dashboard
from pyUR.dashboard import dashboard_commands

class TestDashboard(unittest.TestCase):     
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)

    def setUp(self) -> None:
        pass
          
    def test_dashboard_init(self):
        # arrange
        dashboard.init_socket("192.168.157.128")

        # act
        actual = dashboard.is_connected()
        expected = True

        # assert
        self.assertEqual(actual, expected)

    def test_send_receive_socket(self):
        # arrange
        dashboard.init_socket("192.168.157.128")

        # act
        actual = dashboard.send_receive_socket(dashboard_commands.power_on())
        print(actual)
        expected = "Powering on\n"

        # assert
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()

    
