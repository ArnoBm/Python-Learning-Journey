import random

answer = random.randint(1, 10)
print ("Guess a number between 1 and 10: ")
guess = int(input())

if guess == answer:
    print ("Congratulations! You guessed the number correctly.")
else:
    if guess < answer:
        print ("Please Guess Higher: ")
    else:
        print ("Please Guess Lower: ")
        guess = int(input())
        if guess == answer:
            print ("Congratulations! You guessed the number correctly.")
        else:
            print ("Sorry, you did not guess the number correctly.")
            print (f"The correct answer was {answer}.")