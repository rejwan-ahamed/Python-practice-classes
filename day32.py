# different of set methods in python

a = {1, 3, 5, 7, 44, 3, 4}
b = {44, 66, 74, 22, 44, 22, 4, 5, 7}

c = a.union(b)
d = a.intersection(b)
print(c)
print(a.update(b))
print(d)
e = a.intersection_update(b)
print(a)
