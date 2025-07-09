name = input("Enter your name: ")
age = int(input(f"How old are you, {name}? "))
print (age)

if age >= 110:
    print (f"Don't lie {name}. Take your death certificate and come back to me.")
elif age >= 18:
    print (f"Congratulations {name}, You are an adult now!")
else:
    print (f"You are still a minor {name}, enjoy your childhood! Please come back in {18 - age} years.")