menu = [
    ["milk", "spam", "bread"],
    ["eggs", "butter", "cheese"],
    ["chocolate", "spam", "eggs"],
    ["bread", "milk", "chocolate"],
    ["spam", "cookie", "milk"]
]

for meal in menu:
    for index in range(len(meal)):
        if meal[index] == "spam":
            print("Spam found in meal: ", meal)
            break