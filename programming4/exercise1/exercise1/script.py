print("This program solves the equation ax + b = 0")

a = int(input("Enter an integer for a: "))
b = int(input("Enter another integer for b: "))

print(-b/a)

if a == 0 and b != 0:
    print("The equation has no solution")

elif a == 0 and b ==0:
    print("The equation has infinite solutions")

else:
    solution = -b/a
    print("The solution is", solution)
