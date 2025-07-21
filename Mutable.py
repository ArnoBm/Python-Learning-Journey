shopping_list = ["milk", "eggs", "bread"]
another_list = shopping_list
print (id(shopping_list))
print (id(another_list))

shopping_list += ["butter"]
print (shopping_list)
print (id(shopping_list))

a = b = c = d = e = f = another_list
print(a)

print ("Adding cookies")
b.append ("cookies")
print (e)
print (f)