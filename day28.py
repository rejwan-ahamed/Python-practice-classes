# f string in python

# old approach of f string in python old version
letter = "I am {} and I am a {}. I am the owner of {} companies"

name = "Rejwan Ahamed"
designation = "Bencher capitalist"
owners = "Multi national" 

print(letter.format(name, designation, owners))

# we can play with the index serial in f string
letter2 = "I am {1} and I am a {0}. I am the owner of {2} companies"
print(letter2.format(name, designation, owners))

# new and efficient approach of f string 
print(f"I am {name} and I am a {designation}. I am the owner of {owners} companies")

price = 45.34343

print(f"the total price is {price:.2f}")
