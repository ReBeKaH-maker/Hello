num = int(input("Enter a number:"))
if num % 2 == 0:
    if num > 15 and num < 50 :
        print(num,"is a lucky number")
    else:
     print(num, "is even")
else:
    print(num,"is odd")