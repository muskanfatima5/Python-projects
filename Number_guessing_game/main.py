import random

print("Welcome to the Number Guessing Game! \n You will get 5 chances to guess the number between 50 to 100. \n Let the game begin!")

number_toguess = random.randrange(50, 100)

chances = 5
guess_count = 0

while guess_count < chances:
    guess_count += 1
    my_guess = int(input("Enter your guess no: "))

    if my_guess == number_toguess: 
        print(f" The number is {number_toguess} you guessed the right number in {guess_count} attempt")
        break

    elif guess_count >= chances and my_guess != number_toguess:
        print(f"Sorry! You have used all your chances. The number was {number_toguess}. Better Luck next time!")

    elif my_guess > number_toguess:
        print(f"Your guess is higher than the no. Try again!")

    elif my_guess < number_toguess:
        print(f"Your guess is Lower than the no. Try again!")