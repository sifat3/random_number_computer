import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"guess the number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry, too low.")
        elif guess > random_number:
            print('sorry too high')

    print("you guessed it right")

guess(10)
