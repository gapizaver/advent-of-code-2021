oxygen = []     # possible values for oxygen generator rating
co2 = []        # possible values for co2 scrubber rating

with open("input.txt") as file:
    for line in file:
        oxygen.append(line.rstrip())
        co2.append(line.rstrip())
word_len = len(oxygen[0])

# oxygen search
for i in range(word_len):
    # if only 1 possibility left finish
    if len(oxygen) == 1:
        break

    ones = 0        # number of 1 bits
    zeros = 0       # number of 0 bits
    most_common = 1 # most common bit in current position

    # find the most common bit in that position in oxygen
    for line in oxygen:
        if line[i] == "1":
            ones += 1
        elif line[i] == "0":
            zeros += 1;
    
    if ones < zeros:
        most_common = 0
    
    # only values with the most common bit remain
    oxygen_new = []
    for line in oxygen:
        if int(line[i]) == most_common:
            oxygen_new.append(line)
    oxygen = oxygen_new

# co2 search
for i in range(word_len):
    # if only 1 possibility left finish
    if len(co2) == 1:
        break

    ones = 0        # number of 1 bits
    zeros = 0       # number of 0 bits
    least_common = 0 # most common bit in current position

    # find the most common bit in that position in co2
    for line in co2:
        if line[i] == "1":
            ones += 1
        elif line[i] == "0":
            zeros += 1;
    
    if ones < zeros:
        least_common = 1
    
    # only values with the most common bit remain
    co2_new = []
    for line in co2:
        if int(line[i]) == least_common:
            co2_new.append(line)
    co2 = co2_new

print(oxygen[0])
print(co2[0])
# covert gamma and epsilon to decimal and multiply them
print("result:", int(oxygen[0], 2) * int(co2[0], 2))

