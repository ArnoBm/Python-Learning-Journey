def python_food():
    width = 80
    text = "Pizza and Pasta"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)

def  centre_text(*args, sep=" "):
    text = ""
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text)) // 2
    return " " * left_margin, text

# with open("centred", mode="w") as centred_file:
# call the function
s1 = centre_text("Pizza and Pasta")
print(s1)
s2 = centre_text("Pepsi, Pizza and Pasta")
print(s2)
s3 = centre_text(12)
print(s3)
s4 = centre_text("Pitha, Pepsi, Pizza and Pasta")
print(s4)
s5 = centre_text("First", "Second", 3, 4, "Five", sep=" | ")
print(s5)

print("=" + str(12 *3))
print(sorted(["b", "d", "c", "a"]))
# print("First", "Second", 3, 4, "Five")
# python_food()