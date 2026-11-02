user_money = int(input("Enter the amout of money you have:"))
withdraw_amount = int(input("Enter the amount you want to withdraw:"))
if withdraw_amount > user_money:
    print("Sorry,withdrawal amount is bigger the the amount you have")
else:
   print("You have withdrawn £",withdraw_amount,"and you have £",user_money -  withdraw_amount," left in your account")