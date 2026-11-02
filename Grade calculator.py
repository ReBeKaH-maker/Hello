grade = int(input("Enter you points out of 100:"))
if grade == 100:
print("You got A grade (full marks) ")
elif grade < 100 and grade > 90:
print("You got A grade")
elif grade < 90 and grade > 70:
print("You got B grade")
elif grade < 70 and grade > 50:
print("You got C grade")
elif grade < 50 and grade > 20:
print("You got E grade")
else:
print("You got F grade you did not pass")