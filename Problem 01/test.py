import unittest
from unittest.mock import patch
from timer import Timer
from datetime import date, datetime, timedelta
import time

class TestFunctionTime(unittest.TestCase):

	def test_start_timer(self):
		timer = Timer()
		value = date.today()
		timer.start_timer(value)

		self.assertEqual(timer.get_start_time(), value)

	def test_end_timer(self):
		timer = Timer()
		timer.start_timer()
		value = date.today()
		timer.end_timer(value)

		self.assertEqual(timer.get_end_time(), value)

	@patch('time.sleep', return_value=None)
	def test_duration(self, patched_time_sleep):
		timer = Timer()
		timer.start_timer()
		time.sleep(60)
		timer.end_timer()

		patched_time_sleep.assert_called_once()

	@patch('time.sleep', return_value=None)
	def test_duration_human_readable(self, patched_time_sleep):
		timer = Timer()
		timer.start_timer()
		time.sleep(60)
		timer.end_timer()

		self.assertEqual('Your function was executed in 0 miliseconds.', timer.human_readable_time())
		patched_time_sleep.assert_called_once()

	def test_duration_human_readable_days(self):
		timer = Timer()
		timer.start_time = datetime.today()
		timer.end_time = timer.start_time + timedelta(days=10)
		self.assertEqual('Your function was executed in 10 days.', timer.human_readable_time())

	def test_duration_human_readable_hours(self):
		timer = Timer()
		timer.start_time = datetime.today()
		timer.end_time = timer.start_time + timedelta(hours=10)
		self.assertEqual('Your function was executed in 10 hours.', timer.human_readable_time())

	def test_duration_human_readable_minutes(self):
		timer = Timer()
		timer.start_time = datetime.today()
		timer.end_time = timer.start_time + timedelta(minutes=10)
		self.assertEqual('Your function was executed in 10 minutes.', timer.human_readable_time())

	def test_duration_human_readable_seconds(self):
		timer = Timer()
		timer.start_time = datetime.today()
		timer.end_time = timer.start_time + timedelta(seconds=10)
		self.assertEqual('Your function was executed in 10 seconds.', timer.human_readable_time())

	def test_duration_human_readable_all(self):
		timer = Timer()
		timer.start_time = datetime.today()
		timer.end_time = timer.start_time + timedelta(days=10) + timedelta(hours=10) + timedelta(minutes=10) + timedelta(seconds=10)
		self.assertEqual('Your function was executed in 10 days, 10 hours, 10 minutes, 10 seconds.', timer.human_readable_time())

if __name__ == '__main__':
	unittest.main()

