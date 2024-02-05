inputs = []
for i in range(7):
    inputs.append(input(f"Enter Char: {i+1}: "))
print("#########\n")

f_line = inputs[0] + inputs[1] + inputs[2] + inputs[3]
s_line = inputs[4] + inputs[5]
l_line = inputs[6]

print(f_line, "\n", s_line, "\n", l_line, sep="")