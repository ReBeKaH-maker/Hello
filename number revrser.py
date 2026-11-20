number = 123
reversed_num = 0

while number > 0:
    last_digit = number % 10
    reversed_num = (reversed_num * 10) + last_digit
    number //= 10

print("Output =", reversed_num)  # Prints 321