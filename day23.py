# array methods

numbers = [100, 23, 14, 9, 15, 56, 77, 8, 9]
# print(numbers)

numbers.append(33)
# print(numbers)

numbers.sort()
# print(numbers)

numbers.sort(reverse=True)
# print(numbers)

numbers.reverse()
# print(numbers)

# print(numbers.index(56))

# print(numbers.count(9))

# m = numbers.copy()
# m[0] = 0
# print(m)
# print(numbers)

numbers.insert(4, 200)
# print(numbers)

extraNumbers = [34, 6, 76, 4, 34242, 00]
numbers.extend(extraNumbers)
# print(numbers)

# print(extraNumbers + numbers)

# array comprehensions hacker rank problem solving part

# this is the array comprehensions demo 

result = [x for x in [1,3,4]]

# print(result)

# it's a 2D matrix
result2 = [[x,y] for x in [1,2,3] for y in [3,4,5]]

# print(result2)

# now we are writing the code equivalent to the array comprehensions

result3 = []

for x in [1,2,3]:
    for y in [3,4,5]:
        result3.append([x,y])

# print(result3)

# now the problem solving part


# we are going to solve the problem using the array comprehensions

x=1
y=2
z=1

n=4

final_result = [[i,j,k] for i in range(0,x+1) for j in range(0, y+1) for k in range(0,z+1) if i+j+k !=n]

print(final_result)








