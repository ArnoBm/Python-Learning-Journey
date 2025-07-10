day = "Friday"
temp = 30
raining = True
day_name = input("What day is it? ")
temperature = int(input("What is the temperature? "))

if day_name == day and temperature > temp or not raining:
    print ("It's a good day for outing!")
else:
    print("It's a good day for learning Python!")