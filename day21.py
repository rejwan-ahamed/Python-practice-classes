# default argument in python

def defaultArgument(a, b=3):
    sum = a+b
    print(sum)
defaultArgument(3)


# if we want to get many number of average but dont know how many numbers we will get in the input
# here ue are taking a tuple as an argument and the syntax is *numbers we use * to define a tuple for a function argument

def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    print("Average is :", sum/len(numbers))


average(2, 4, 5, 30, 50)
