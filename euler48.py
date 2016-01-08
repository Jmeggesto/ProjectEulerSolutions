import platform

if platform.python_version() > "2.7.10":
	from functools import reduce

self_power_sum = reduce(lambda x, y: x+y, [x ** x for x in range(1, 1001)])
print(str(self_power_sum)[-10:])