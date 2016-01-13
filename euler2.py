""" fibonacci_array = [1, 2]
sumvar = 2
while fibonacci_array[-1] < 4000000:
	next_item = fibonacci_array[-1] + fibonacci_array[-2]
	fibonacci_array.append(next_item)
	if next_item % 2 == 0:
		sumvar += next_item

print(sumvar)
"""
a = 1
b = 2
sumvar = 2
next_item = a + b 
while next_item < 4000000:
	
	if next_item % 2 == 0:
		sumvar += next_item
	a = b
	b = next_item
	next_item = a + b 

print(sumvar)