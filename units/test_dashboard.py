import unittest
from unittest import mock
from pyUR.dashboard.dashboard import dashboard
from pyUR.dashboard.dashboard_commands import dashboard_commands

class TestDashboard(unittest.TestCase):     
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)

    def setUp(self) -> None:
        pass
          
    def test_dashboard_init(self):
        # arrange
        self.dashboard = dashboard("192.168.1.8")

        # act

        # assert

    def test_send_receive_socket(self):
        # arrange
        self.dashboard = dashboard("192.168.157.128")
        mock_socket = mock.Mock()
        mock_socket.connect.return_value = "Powering on"

        # act
        print("Sending power on command: " + dashboard_commands.commands["power_on"])
        received = self.dashboard.send_receive_socket(dashboard_commands.commands["power_on"])

        # assert
        self.assertEqual(received, "Powering on")


if __name__ == '__main__':
    unittest.main()

    
