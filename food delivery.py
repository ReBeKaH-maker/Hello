##Ask the user to choose a food item and quantity. Calculate the subtotal, apply free delivery for orders of n500
##or more (otherwise add n40), and print the final bill. Use variables, operators, if-else, and suitable data types.
food = input("Please choose a food item:")
quantity = int(input("Please enter the quantity:"))
total == quantity * 4
if total >= 500:
    delivery_fee = 0
    print("You get free delivery! you total is",total)
else: 
    delivery_fee = 40
    print("You have a delivery fee of ",delivery_fee,"your total is",total + delivery_fee)