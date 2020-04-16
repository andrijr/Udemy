a = "tekst"
print(a)
print(type(a))
print(a[1])
print(dir())
#print(help())
print(a[0], a[1])

for i in a:
    print("{:10}".format(a), end="  ")
print()

print(a[0:3])