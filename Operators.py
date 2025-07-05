a = int(input("Enter the fist number: "))
b = int(input("Enter the second number: "))

print ("Answer in Sum: ", a+b)
print ("Answer in Min: ", a-b)
print ("Answer in Mul: ", a*b)
print ("Answer in Div(float): ", a/b)     #Float division
print ("Answer in Div(integer): ", a//b)    #integer division
print ("Answer in Modulus: ", a%b)     #modulus

print()

for i in range(1, a//b):
    print(i)