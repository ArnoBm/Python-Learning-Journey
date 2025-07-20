numbers = [1, 45, 37, 17, 58]

for number in numbers:
    if number % 2 == 0:
        print(f"{number} is even.")
        break
    else:
        print(f"{number} is odd.")