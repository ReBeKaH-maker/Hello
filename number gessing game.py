number = 16
for i in range(5):
    guess = int(input("Guess the number it's between 1 and 20:"))
    if guess == number:
        print("You guessed it right! in",i+1,"tries")
        break
    elif guess < number:
        print("It's higher than that")
    elif guess > number:
        print("It's lower than that")
    else:
        print("You lost! the number was ",number)
      