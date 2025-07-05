name = input("Enter your name: ")
age = int(input("Enter your age: "))

print ("Hello, I am {0} and I am {1} years old.".format (name, age))  # Output: Hello, I am <name> and I am <age> years old.

days = 31
print ("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6}, and {7}.".format(days,"Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"))  # Output: There are 31 days in Jan,Mar,May,Jul,Aug,Oct,Dec.
print ("Jan: {2} \nFeb: {0} \nMar: {2} \nApr: {1} \nMay: {2} \nJun: {1} \nJul: {2} \nAug: {2} \nSep: {1} \nOct: {2} \nNov: {1} \nDec: {2}"
       .format(28, 30, 31))  # Output: Jan: 31, Feb: 28, Mar: 31, Apr: 30, May: 31, Jun: 30, Jul: 31, Aug: 31, Sep: 30, Oct: 31, Nov: 30, Dec: 31