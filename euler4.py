products_of_3_digit_numbers = [( x * y) for x in range(100, 1000) for y in range(100, 1000)]
palindromic_numbers = [x for x in products_of_3_digit_numbers if str(x)[::-1] == str(x)]
max_palindrome_product = max(palindromic_numbers)
print(max_palindrome_product)