shopping_list = ["milk", "eggs", "bread", "butter", "cheese", "apples", "bananas"]
for item in shopping_list:
    if item == "bread":
        print("Bread is out of stock, skipping.")
        continue
    print(f"Buy {item} from the store.")