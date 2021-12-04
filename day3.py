input = []

with open("input.txt") as file:
    for line in file:
        input.append(line.rstrip())

gamma = ""
epsilon = ""

for i in range(len(input[0])):
    ones = 0        # number of 1 bits
    zeros = 0        # number of 0 bits

    # find the most common bit in that position
    for line in input:
        if line[i] == "1":
            ones += 1
        elif line[i] == "0":
            zeros += 1;
    
    if ones > zeros:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

# covert gamma and epsilon to decimal and multiply them
print("result:", int(gamma, 2) * int(epsilon, 2))
