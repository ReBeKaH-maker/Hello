#An amusement park ride requires a visitor to be at least 120 cm tall and at least 10 years old.
hight = int((input("Enter your hight in cetmeters:")))
age = int((input("Enter you age:")))
if hight >= 120 and age >= 10 :
    print("Your alowed come right in enjoy")
else:
    print("sorry you can't come in mabye when your older")