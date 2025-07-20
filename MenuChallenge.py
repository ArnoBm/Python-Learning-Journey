print ("Please choose a option from the menu below:")
print ("1. Learn Python")
print ("2. Learn Java")
print ("3. Learn C++")
print ("4. Learn C#")
print ("5. Learn C")
print ("0. Exit")

while True:
    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        print("You chose to learn Python!")
    elif choice == '2':
        print("You chose to learn Java!")
    elif choice == '3':
        print("You chose to learn C++!")
    elif choice == '4':
        print("You chose to learn C#!")
    elif choice == '5':
        print("You chose to learn C!")
    elif choice == '0':
        print("Exiting the menu. Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")