# distinct_powers = set([i ** j for i in range(2, 101) for j in range(2, 101)])


for i in range(2, 101):
	for j in range(2, 101):
		if i ** j not in distinct_powers:
			distinct_powers.append(i **j)

print(len(distinct_powers))