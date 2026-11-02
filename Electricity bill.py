#A household's electricity bill is calculated using units consumed: up to 100 units = n3 per unit; 101–200 units= n5 per unit; above 200 units = n8 per unit. Ask for units and calculate the bill using if-elif-else.
electricty = int((input("Enter The units you have used")))
if electricty <= 100:
    print("You have to pay n3 per unit")
elif electricty > 101 and electricty < 200 :
    print("You have to pay n5 per unit")
elif electricty > 200 :
    print("You have to pay n8 per unit")