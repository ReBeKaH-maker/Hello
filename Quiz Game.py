# Question 1
qestion1 = int(input("What is 10 x 10?: "))
if qestion1 == 100:
    print("Correct!\n")
else:
    print("Incorrect!\n")

# Question 2
qestion2 = input("What is the capital of England?: ")
if qestion2.lower() == "london":
    print("Correct!\n")
else:
    print("Incorrect!\n")

# Question 3
qestion3 = input("Are insects vertebrates or invertebrates?: ")
if qestion3.lower() == "invertebrates":
    print("Correct! 2 more to go!\n")
else:
    print("Incorrect!\n")

# Question 4
qestion4 = input("When is Christmas?: ")
if "december 25" in qestion4.lower():
    print("Correct! Only 1 more to go!")
else:
    print("Incorrect!")

# Question 5
qestion5 = input("how long is one year ( Just the days :) )  : ")
if "365" in qestion5.lower():
    print("Correct! you fineshed the quiz well done :)!")
else:
    print("Incorrect! you were so close :(")