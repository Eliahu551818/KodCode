import math
radius = input("Enter the radius of a circle: ")

while not radius.isdigit():
    radius = input("Enter the radius of a circle: ")

radius_as_int = int(radius)

pi = math.pi
area = pi*radius_as_int**2
circumferrence = 2*pi*radius_as_int

print("\n\n###################################################\n")
print("The radius of your circle equals to: ", radius)
print("The area of your circle equals to: ", area)
print("The circumferrence of your circle equals to: ", circumferrence)
print("\n###################################################\n\n")
