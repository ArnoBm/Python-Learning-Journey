name = input("Write your name: ")
age = int(input("Write your age: "))

if 18 <= age < 31:
    print (f"Hello {name}, you are eligible to this holiday party.")
else:
    print (f"Hello {name}, you are not eligible to this holiday party.")