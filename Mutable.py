shopping_list = ["milk", "eggs", "bread"]
another_list = shopping_list
print (id(shopping_list))
print (id(another_list))

shopping_list += ["butter"]
print (shopping_list)
print (id(shopping_list))