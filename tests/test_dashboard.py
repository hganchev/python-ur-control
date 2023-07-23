import unittest
from unittest import mock
from pyUR.dashboard import dashboard, dashboard_commands

class TestDashboard(unittest.TestCase):     
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)

    def setUp(self) -> None:
        pass

    def test_connected(self):
        # arrange
        dashboard._connected = True

        # act
        actual = dashboard.is_connected()
        expected = True

        # assert
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()

    
