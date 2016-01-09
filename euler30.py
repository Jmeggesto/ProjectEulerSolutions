def DigitFifthPower(number):
	return sum([int(digit) ** 5 for digit in str(number)]) == number

fifth_power_arr = [x for x in range(2, 1000000) if DigitFifthPower(x)]
print(sum(fifth_power_arr))
