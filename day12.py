# string method
# 1. string slicing
# 2. length function ********* len() it return a integer value and take a argument as string which it calculate the length


name = "Rejwan Ahamed"
print(name[0:6])
print("length of the string:", len(name))

fruit = "mango"
print(fruit[-4: -2])

# the code returning "an" because
# first the code will check the length of the string and the total length of "fruit" string is =5
# the the code subtract length - 4 = 1, again length - 2 = 3
# the result of the code is {print(fruit[1:3])} = an