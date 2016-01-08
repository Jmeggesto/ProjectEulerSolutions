import platform

if platform.python_version() > "2.7.10":
	from functools import reduce

sum_of_digits = reduce(lambda x, y: x + y, [int(x) for x in str(2 ** 1000)])
print(sum_of_digits)