units = float((input("enter the number of units consumed:")))
if units < 50 :
 bill = units * 2.6
 tax = 25 
elif units > 50 and  units < 100:
 bill = units * 3.35
 tax = 35
elif units < 200 and units > 100:
 bill = units * 4.5
 tax = 45 
else:
 bill = units * 8.45
 tax = 75
print("The total bill is:",bill + tax)