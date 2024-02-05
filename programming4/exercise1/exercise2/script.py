print("\n\n###### Eliahu's Checker ######")
num = input("Enter a number higher than 0, with multiple digits: ")

while True:
    if len(num) <= 1:
        num = input("Please enter a sequence not a single digit: ")

    elif int(num) <= 0:
        num = input("Please use a sequence of numbers higher than 0: ")
    
    else:
        break

res = True
for i in range(1,len(num)):
    if num[i] <= num[i-1]:
        res = False
        break

print("Your result:", res)