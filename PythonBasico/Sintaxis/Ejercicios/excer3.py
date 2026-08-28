import random;

secret_number = random.randint(1, 10)
guess = False


if guess == False:
    while not guess:
        tryGuess = int(input("Please guess a number between 1 and 10: "))
        if tryGuess < 1 or tryGuess > 10:
            print("Invalid input. Please enter a number between 1 and 10.")
            
        elif tryGuess == secret_number:
            print("Congratulations! You guessed the correct number.")
            guess = True
        elif tryGuess < secret_number:
            print("Your guess is too low. Try again.")
        else:
            print("Your guess is too high. Try again.")

1