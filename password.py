print("The password is 10 x my age + 10")
age = 10
print("Hint: my age is", age)

# Use 'user_input' to avoid breaking Python's built-in input() function
user_input = int(input("Enter the password: "))

if user_input == 10 * age + 10:
    print("Access granted! Welcome back!")
    num = int(input("Enter a number: "))
    
    # num % 2 checks for even/odd numbers
    if num % 2 == 0:
        print(num, "is even")
    else:
        print(num, "is odd")
else:
    print("Error 404: try again")