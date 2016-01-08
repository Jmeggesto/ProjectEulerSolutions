sum_of_squares_to_100 = sum([(x **2) for x in range(0, 101)])
square_of_sum_to_100 = sum([x for x in range(0, 101)]) ** 2
difference = square_of_sum_to_100 - sum_of_squares_to_100
print(difference)