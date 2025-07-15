import random

answer = random.randint(1, 10)
guess = 0
print ("Guess a number between 1 and 10: ")
while guess != answer:
    guess = int(input("Enter your guess: "))
    if guess == answer:
        print("Well done! You guessed the number.")
        break
    else:
        if guess < answer:
            print("Please guess higher.")
        else:
            print("Please guess lower.")