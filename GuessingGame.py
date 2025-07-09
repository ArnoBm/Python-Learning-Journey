import random
randnum = random.randint(1, 10)
while True:
    answer = int(input("Guess a number between 1 and 10: "))
    if answer < randnum:
        print("Please guess higher.")
    elif answer > randnum:
        print("Please guess lower.")
    else:
        print("🎉 Congratulations! You got the correct answer!")
    break