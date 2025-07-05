#                   1111
#         01234567890123
parrot = "Norwegian Blue"

# Slicing with step || Start at index 0, end at index 6, step by 2
print (parrot[0:6:2])  # Output: 'Nge'

# Slicing with step || Start at index 0, end at index 6, step by 3
print (parrot[0:6:3])  # Output: 'Nw'

print(parrot[1::2])  # Output: 'owga le' (every second character starting from index 1)

numbers = "1,755:792;803,123"
separators = numbers[1::4]
print (separators)  # Output: ,:;,

values = "".join(char if char not in separators else " " for char in numbers).split()
print ([int(val) for val in values])  # Output: [1, 755, 792, 803, 123]