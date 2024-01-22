import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number form 1 to {x}: "))
        if guess < random_number:
            print("Your numer is to low!")
        elif guess > random_number:
            print("Your numer is to high!")

    print("Nice you won !!")

