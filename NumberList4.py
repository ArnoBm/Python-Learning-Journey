empty_list = []
odd = [1, 3, 5, 7, 9]
even = [2, 4, 6, 8, 10]

numbers = [odd, even]
print (numbers)

#numbers = odd + even
#print (numbers)

for number_list in numbers:
    print (number_list)

    for value in number_list:
        print (value)