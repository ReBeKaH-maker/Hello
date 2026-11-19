number = 370 
sum = 0
while number :
    last_digit = number % 10
    cube = last_digit ** 3
    sum = sum + cube
    number = number // 10
print(sum)