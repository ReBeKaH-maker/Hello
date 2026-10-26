usedmoney = float(input("Enter the amout of money for the invesment: "))
sellingprice = float(input("Enter the selling price :"))
if sellingprice > usedmoney:
    print("The profit is:", sellingprice - usedmoney)
else:
    print("The loss is :", usedmoney - sellingprice)