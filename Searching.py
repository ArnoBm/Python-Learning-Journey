name = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Judy", "Karl"]

name_to_find = "Heidi"
found_at = None

if name_to_find in name:
    found_at = name.index(name_to_find)

if found_at is not None:
    print(f"{name_to_find} found at index {found_at}")
else:
    print(f"{name_to_find} not found in the list")