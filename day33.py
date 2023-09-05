# dictionary in python

dic = {
    'name': "Rejwan Ahamed",
    'roll': "016",
    'section': "B"
}

print(dic['name'])
print(dic.keys())

# printing the dictionary using for loop
for key in dic.keys():
    print(key + ":" +dic[key])


print(dic.items())


# printing the dictionary using the key value payer

for key, value in dic.items():
    print(key + ":" + value)
