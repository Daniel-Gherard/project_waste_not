import time
from datetime import timedelta, datetime

class Timer():

	def __init__(self):
		self.start_time = None
		self.end_time = None
		
	def start_timer(self, value = time.process_time()):
		self.start_time = value
		
	def get_start_time(self):
		return self.start_time
		
	def end_timer(self, value = time.process_time()):
		self.end_time = value
		
	def get_end_time(self):
		return self.end_time
		
	def duration(self):
		duration = self.get_end_time() - self.get_start_time()
		if (isinstance(duration, timedelta)): return duration.total_seconds()
		else: return 0
	
	def human_readable_time(self, duration = None):
		if duration: duration = timedelta(seconds=duration)
		else: duration = timedelta(seconds=self.duration())
		date = datetime(1,1,1) + duration

		string = 'Your function was executed in '

		days = self.human_readable_time_manager(date.day-1, 'day', 'days')
		hours = self.human_readable_time_manager(date.hour, 'hour', 'hours')
		minutes = self.human_readable_time_manager(date.minute, 'minute', 'minutes')
		seconds = self.human_readable_time_manager(date.second, 'second', 'seconds')
		zeroable = days == '' and hours == '' and minutes == '' and seconds == ''
		miliseconds = self.human_readable_time_manager(date.microsecond, 'milisecond', 'miliseconds', zeroable)

		if (days != ''): string += days
		if (hours != ''): string += self.prepend_spacer(string) + hours
		if (minutes != ''): string += self.prepend_spacer(string) + minutes
		if (seconds != ''): string += self.prepend_spacer(string) + seconds
		if (miliseconds != ''): string += self.prepend_spacer(string) + miliseconds

		string += '.'

		return string

	def prepend_spacer(self, string):
		return ', ' if string != 'Your function was executed in ' else ''

	def human_readable_time_manager(self, value, singular_text, plural_text, zeroable = False):
		string = ''

		if value > 0 or (zeroable and value >= 0):
			string = f'{ value } '

			if value == 1: string += f'{singular_text}'
			else: string += f'{plural_text}'

		return string
