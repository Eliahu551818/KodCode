x,y,z = input("Enter three numbers separated by space: ").split(" ")
x = int(x)
y = int(y)
z = int(z)

print(x/y, x//y, x%y, sep="\t")
print(x/z, x//z, x%z, sep="\t")
print(z/y, z//y, z%y, sep="\t")
