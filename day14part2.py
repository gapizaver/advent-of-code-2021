# Read input
import collections
from math import ceil


# Pair insertion rules
pair_insertions = dict()
# Quantity of element pairs in polymer
pair_quantity = collections.defaultdict(int)

with open("input.txt") as file:
    for line in file:
        if line.rstrip() != "":
            stripped = line.rstrip().split(" -> ")
            if len(stripped) == 1:
                # Count current element pairs
                for i, element in enumerate(stripped[0][:-1]):
                    pair_quantity[element + stripped[0][i+1]] += 1
            else:
                # Add pair insertion rule
                pair_insertions[stripped[0]] = stripped[1]


# Apply 10 steps of insertion to the polymer
for step in range(40):
    new_pair_quantity = pair_quantity.copy()
    # print(pair_quantity)

    # For every pair of elements insert new on between them
    for pair, quantity in pair_quantity.items():
        element_to_insert = pair_insertions[pair] 
        new_pair_quantity[pair[0] + element_to_insert] += 1 * quantity
        new_pair_quantity[element_to_insert + pair[1]] += 1 * quantity
        new_pair_quantity[pair] -= 1 * quantity
    
    pair_quantity = new_pair_quantity.copy()
    # print(pair_quantity)

# Find the least and the most common element
elements_quantity = collections.defaultdict(int)
for pair, quantity in pair_quantity.items():
    elements_quantity[pair[0]] += quantity
    elements_quantity[pair[1]] += quantity

# Correct elements_quantities - they were counted as pairs, so there are twice too many
for element, quantity in elements_quantity.items():
    elements_quantity[element] = ceil(quantity / 2)

# Print result
print(max(elements_quantity.values()) - min(elements_quantity.values()))