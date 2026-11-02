password == 13579
for i in range(3):
 password_input = int(input("Enter the password:"))
 if password_input == password:
  print("Access granted welcome back!")
 elif password_input != password:
  print("Acces denied you have",i,"attempts left")
else:
 print("You have no attempts left")
