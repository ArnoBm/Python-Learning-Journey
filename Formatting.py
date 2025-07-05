start_range = int(input("Enter the starting number: "))
end_range = int(input("Enter the ending number: "))

for i in range (start_range, end_range + 1):
    print ("No. {0} squared is {1} and cubed is {2}".format(i, i**2, i**3))

table = int(input("Enter a number to see its multiplication table: "))
print ("Multiplication table for {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}".format(table, table*2, table*3, table*4, table*5, table*6, table*7, table*8, table*9, table*10))