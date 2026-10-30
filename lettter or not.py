letter = input("enter anything:")

if letter.isalpha():
    print(letter, "is a letter")
elif letter.isdigit():
    print(letter, "is a number")
else:
    print(letter, "is something else")


