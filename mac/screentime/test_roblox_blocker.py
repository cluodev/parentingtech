import unittest
from unittest.mock import patch
from datetime import datetime
import roblox_blocker as rb

class TestRobloxBlocker(unittest.TestCase):
    @patch('roblox_blocker.get_available_times_by_dayOfWeek')
    @patch('roblox_blocker.datetime')
    def test_is_blocking_time(self, mock_datetime, mock_get_times):
        # Setup mock available times
        mock_get_times.return_value = {
            'Monday': [(10, 12), (16, 17)],
        }
        # Test during blocking time (e.g., 9:00)
        mock_datetime.now.return_value = datetime(2025, 6, 16, 9, 0)  # Monday 9:00
        mock_datetime.strftime = datetime.strftime
        self.assertTrue(rb.is_blocking_time())

        # Test during unblocking time (e.g., 10:30)
        mock_datetime.now.return_value = datetime(2025, 6, 16, 10, 30)  # Monday 10:30
        self.assertFalse(rb.is_blocking_time())

        # Test at the exact start of unblocking (10:00)
        mock_datetime.now.return_value = datetime(2025, 6, 16, 10, 0)  # Monday 10:00
        self.assertFalse(rb.is_blocking_time())

        # Test at the exact end of unblocking (12:00)
        mock_datetime.now.return_value = datetime(2025, 6, 16, 12, 0)  # Monday 12:00
        self.assertTrue(rb.is_blocking_time())

        # Test after unblocking (13:00)
        mock_datetime.now.return_value = datetime(2025, 6, 16, 13, 0)  # Monday 13:00
        self.assertTrue(rb.is_blocking_time(), "13:00 should block")

if __name__ == '__main__':
    unittest.main()
