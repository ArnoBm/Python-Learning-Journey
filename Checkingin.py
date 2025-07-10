string = "Practice makes a man perfect"
letter = input("Enter a character: ")

if letter in string:
    print(f"{letter} is in the string which I stored in the variable string")
else:
    print(f"{letter} is not in the string which I stored in the variable string")