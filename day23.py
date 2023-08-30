# array methods

numbers = [100, 23, 14, 9, 15, 56, 77, 8, 9]
print(numbers)

numbers.append(33)
print(numbers)

numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

numbers.reverse()
print(numbers)

print(numbers.index(56))

print(numbers.count(9))

# m = numbers.copy()
# m[0] = 0
# print(m)
# print(numbers)

numbers.insert(4, 200)
print(numbers)

extraNumbers = [34, 6, 76, 4, 34242, 00]
numbers.extend(extraNumbers)
print(numbers)

print(extraNumbers + numbers)
