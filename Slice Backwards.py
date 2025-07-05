#                    1111111111222222
#          01234567890123456789012345
letters = "abcdefghijklmnopqrstuvwxyz"
backwards = letters[25::-1] # Slicing backwards || Start at index 25, no end index, step by -1
print (backwards)  # Output: 'zyxwvutsrqponmlkjihgfedcba'

# Create a slice that produces the chacarters qpo
backwards1 = letters[16:13:-1]
print (backwards1) # Output: 'qpo'

# Slice the string to produce edbca
backwards2 = letters[4::-1]
print (backwards2)  # Output: 'edcba'

# Slice the string to produce the last 8 characters in reverse order
backwards3 = letters[25:17:-1]
print (backwards3) # Output: 'zyxwvuts'