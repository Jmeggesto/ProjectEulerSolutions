
numdigitstr = ""
numToAppend = 1
while len(numdigitstr) < 1000000:
    numdigitstr += str(numToAppend)
    numToAppend += 1


product = 1
for i in range(1, 7):
	product *= int(numdigitstr[(10 ** i) -1])

print(product)
