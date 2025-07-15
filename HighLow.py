low = 1
high = 1000

print (f"Please guess a number between {low} and {high}: ")
input ("Press Enter to start...")
guesses = 1
while True:
    guess = low + (high - low) // 2
    high_low = input(f"Is your number {guess}? (h/l/c): ").casefold()
    if high_low == "h":
        low = guess + 1
    elif high_low == "l":
        high = guess - 1
    elif high_low == "c":
        print(f"Yay! Your number is {guess}.")
        break
    else:
        print("Invalid input. Please enter 'h' for higher, 'l' for lower, or 'c' for correct.")

        guesses = guesses + 1