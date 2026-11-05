#Ask how many expenses the user wants to enter. Use a loop to collect each expense and calculate the total.
#then use if-else to display 'Within budget' if the total is n2,000 or less, otherwise display 'Budget exceeded
expenses = int(input("How many expenses do you want to enter?:"))
for i in range(expenses):
    expense = float(input("Enter expense amount:"))
if expense <= 2000:
    print("your within budget")
else:
    print("Budget exceeded")