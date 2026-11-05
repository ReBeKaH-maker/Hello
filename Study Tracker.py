total_hours = 0

for i in range(1, 8):  # Days 1 to 7
    hours = int(input("Enter the number of hours you studied on day {i}: "))
    total_hours += hours

average = total_hours / 7

print("Total study time for 7 days:", total_hours, "hours")
print("Average study time per day:", average, "hours")