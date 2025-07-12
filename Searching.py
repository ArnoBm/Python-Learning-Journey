name = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Judy", "Karl"]

name_to_find = "Heidi"
found_at = None

for index in range(len(name)):
    if name[index] == name_to_find:
        found_at = index
print (f"{name_to_find} is found at index {found_at}")