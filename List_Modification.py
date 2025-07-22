my_list = []

def display_menu():
    print("\n--- List Operation Menu ---")
    print("1. Insert item")
    print("2. Update item")
    print("3. Delete item")
    print("4. Show list")
    print("5. Exit")

while True:
    display_menu()
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        item = input("Enter item to insert: ")
        my_list.append(item)
        print(f"'{item}' inserted.")

    elif choice == "2":
        if not my_list:
            print("List is empty. Nothing to update.")
        else:
            print("Current list:", my_list)
            try:
                index = int(input("Enter index to update (starting from 0): "))
                if 0 <= index < len(my_list):
                    new_value = input("Enter new value: ")
                    my_list[index] = new_value
                    print("Item updated.")
                else:
                    print("Invalid index.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "3":
        if not my_list:
            print("List is empty. Nothing to delete.")
        else:
            print("Current list:", my_list)
            try:
                index = int(input("Enter index to delete (starting from 0): "))
                if 0 <= index < len(my_list):
                    removed = my_list.pop(index)
                    print(f"'{removed}' deleted.")
                else:
                    print("Invalid index.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":
        print("Current list:", my_list)

    elif choice == "5":
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid option. Please choose between 1 and 5.")
