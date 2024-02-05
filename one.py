num = input("Enter a number: ")

while num.isdigit() == False:
    num = input("Enter a number: ")

num = int(num)
if num > 10:
    print("The number is greater than 10")
elif 0 < num < 10:
    print("The number is between 0 and 10")
elif num <= 0:
    print("The number is less than or equal to 0")