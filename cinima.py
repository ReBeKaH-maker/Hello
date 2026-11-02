tickets = int(input("Enter the number of tickets you want to buy:"))
movie = input("Enter the movie name:")
membership_input = input("Are you part of our membership? (True/False):").strip().lower()
membership = membership_input == "true"

if membership:
    price = 2 * tickets
    print("Your total price to watch", movie, "is:", price, "£")
else:
    price = 4 * tickets
    print("Your total price to watch", movie, "is:", price, "£") 