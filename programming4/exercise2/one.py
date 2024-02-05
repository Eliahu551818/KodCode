num_as_str = input("Enter a number with 3 digits: ")

while len(num_as_str) != 3:
    num_as_str = input("Enter a number with 3 digits: ")

num_as_int = int(num_as_str)

# sum the tens and ones digits and subtract the hundreds digit

meot = num_as_int//100
asarot = (num_as_int//10)%10
achadot = num_as_int%10

print("The sum of the tens and ones digits minus the hundreds digit is:", asarot-(meot+achadot))