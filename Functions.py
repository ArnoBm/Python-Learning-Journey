def multiply(x, y):
    result = x * y
    return result

def is_palindrome(string):
    # backwards = string[::-1]
    # return backwards == string
    return string[::-1].casefold() == string.casefold()

# answer = multiply(10.5, 4)
# print(answer)
#
# forty_two = multiply(6, 7)
# print(forty_two)
#
# print("-"*10)
#
# for val in range(1, 5):
#     two_times = multiply(2, val)
#     print(two_times)
def palindrom_sentence(sentence):
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char

    # return string[::-1].casefold() == string.casefold()
    return is_palindrome(string)

word = input("Enter a word: ")
if palindrom_sentence(word):
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")