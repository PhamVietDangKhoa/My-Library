myString = "This is a string."
print(myString)
print(type(myString))
print(myString + " is of the data type " + str(type(myString)))
firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)

name = input("What is your name? ")
color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")
age = input("How old are you? ")
name1 = input("What is your wife name? ")
age1 = input("And How old your wife ?")
print("{},you are {} and you like a {} {}!".format(name,age,color,animal))
print("Your wife name is {} and she's {}".format(name1,age1))