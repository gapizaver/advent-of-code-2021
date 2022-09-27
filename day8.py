# Read input
input = []
with open("input.txt") as file:
    for line in file:
        input.append(line.rstrip().split(" | "))

# Split input lines into arrays of words
lines = []
for line in input:
    lines.append([line[0].split(), line[1].split()])

# Count digits 1, 4, 7, 8 (lengths 2, 4, 3, 7)
counter = 0
for line in lines:
    for word in line[1]:
        if len(word) in [2, 3, 4, 7]:
            counter += 1

# Print solution
print(counter)