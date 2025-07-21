separators = (" ", ".", ",", ":", ";", "/", "-")

odd = input("Enter Odd Numbers: ")
even = input("Enter Even Numbers: ")

def extract_numbers(text):
    for sep in separators:
        text = text.replace(sep, " ")
    numbers = [int(num) for num in text.split() if num.isdigit()]
    return numbers

odd_numbers = extract_numbers(odd)
even_numbers = extract_numbers(even)

only_odds = [num for num in odd_numbers if num % 2 != 0]
only_evens = [num for num in even_numbers if num % 2 == 0]

print("\n✅ Given Odd Number Set: ", only_odds)
print("🔺 Highest Odd Number: ", max(only_odds))
print("🔻 Lowest Odd Number: ", min(only_odds))
print("📏 Total Odd Numbers: ", len(only_odds))

print("\n✅ Given Even Number Set: ", only_evens)
print("🔺 Highest Even Number: ", max(only_evens))
print("🔻 Lowest Even Number: ", min(only_evens))
print("📏 Total Even Numbers: ", len(only_evens))
