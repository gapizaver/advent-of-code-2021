# Read input
import collections


polymer = ""
pair_insertions = dict()
with open("input2.txt") as file:
    for line in file:
        if line.rstrip() != "":
            stripped = line.rstrip().split(" -> ")
            if len(stripped) == 1:
                polymer = stripped[0]
            else:
                pair_insertions[stripped[0]] = stripped[1]

# Apply 10 steps of insertion to the polymer
for step in range(20):
    # For every pair of elements insert new on between them
    polymer_new = polymer
    num_of_inserted = 0

    for i, element in enumerate(polymer[:-1]):
        pair = element + polymer[i+1]
        if pair in pair_insertions.keys():
            polymer_new = polymer_new[:i + num_of_inserted + 1] + \
                    pair_insertions[pair] + polymer_new[i + num_of_inserted + 1:]
            num_of_inserted += 1

    polymer = polymer_new 
    print(step)


# Find the least and the most common element
num_of_elements = collections.defaultdict(int)
for element in polymer:
    num_of_elements[element] += 1

# Print result
print(max(num_of_elements.values()) - min(num_of_elements.values()))