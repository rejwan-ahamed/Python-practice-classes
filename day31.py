# recursion function
# recursive function call itself

def factorial(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * factorial(n-1)


a = int(input("Enter a number: "))

b = factorial(a)
print(b)