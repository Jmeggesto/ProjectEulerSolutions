import math

def Composite(number):

	for i in range(2, int(math.sqrt(number))):
		if number % i == 0:
			return True
			break

	return False

a = [x for x in range(0, 100) if Composite(x)]
print(a)