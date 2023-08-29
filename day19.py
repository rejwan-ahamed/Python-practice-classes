# break case in for loop

for a in range(10):
    print(a)
    if (a == 5):
        break

# continue case in for loop

for i in range(10):
    if (i == 6):
        continue
    print(i)


# beak case in while loop
a = 1
while (a < 10):
    if (a == 4):
        break
    print(a)
    a = a+1


# continue in while loop
b = 1
while (b < 10):
    if (b == 5):
        continue
    print(b)
    b = b+1
