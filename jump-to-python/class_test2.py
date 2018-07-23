class Family:
    lastname = "김"


a = Family()
b = Family()

print(a.lastname)
print(b.lastname)


Family.lastname = "박"
print(a.lastname)
print(b.lastname)