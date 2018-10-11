from random import randint

num = randint(0,6)

guess = int(input('Guess the numbers from 0 to 6 '))

while True:
    
    if num < guess:
        print("your guess is too high")
        guess = input("Guess again\n")
    elif num> guess:
        print("your guess is too low\n")
        guess = input("Guess again")
    elif num == guess:
        print("correct guess")
