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

only_evens.extend(only_odds)
print ("Extended Even Numbers: ", only_evens)

only_evens.sort()
print ("Extended Odd Numbers: ", only_evens)

only_evens.sort(reverse=True)
print ("Extended Odd Numbers: ", only_evens)