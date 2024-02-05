num = int(input("Enter a number lower than 11, higher than 0: "))

while not 0 < num < 10:
    num = int(input("Enter a number lower than 11, higher than 0: "))

for i in range(1, num + 1):
    line = ""
    multiplier = 1
    
    while multiplier <= num:
        line += f"{i*multiplier}\t"
        multiplier += 1
    
    print(line)   