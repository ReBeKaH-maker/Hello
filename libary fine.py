##Ask how many days late a library book is. No fine is charged for 0 days. Charge n2 per day for the first 5 late days and n5 per day for each additional day. Calculate and display the fine.
days = int(input("Enter the number of days late:"))
if days == 0 :
    print("No fine charged.")
elif days <= 5:
    fine = days * 2
    print("The fine is:",fine) 
else:
    fine = 10 + days * 5
    print("The fine is:",fine)