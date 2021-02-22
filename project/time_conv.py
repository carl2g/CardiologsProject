import time


def date_time_to_sec(t: str):
	return time.mktime(time.strptime(t, "%H:%M:%S %d/%m/%y"))


def sec_offset(start: str, end: str):
	return date_time_to_sec(end) - date_time_to_sec(start)


def sec_to_ms(sec: int):
	return sec * 1000


def sec_to_date_time(sec: int):
	return time.strftime("%H:%M:%S %d/%m/%y", time.localtime(sec))
