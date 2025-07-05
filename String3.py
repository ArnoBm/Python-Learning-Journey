name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")

# f-strings (Python 3.6+) Easy and readable way to format strings
print (f"Hello my name is {name}, and I am {age} years old. I live in {city}.") #Output: Hello my name is <name>, and I am <age> years old. I live in <city>.
# Old-style formatting
print ("hello my name is %s, and I am %d years old. I live in %s." % (name, age, city)) #Output: hello my name is <name>, and I am <age> years old. I live in <city>.
# str.format() method
print ("hello my name is {}, and I am {} years old. I live in {}.".format(name, age, city)) #Output: hello my name is <name>, and I am <age> years old. I live in <city>.
