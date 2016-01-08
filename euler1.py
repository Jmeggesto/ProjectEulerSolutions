import platform
if platform.python_version() > "2.7.10":
	from functools import reduce	



a = reduce(lambda x, y: x + y, [x for x in range(1, 1000) if x % 3 == 0 or x % 5 == 0])
print(a)