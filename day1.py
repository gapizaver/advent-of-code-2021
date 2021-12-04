input = []

with open("input.txt") as file:
    for line in file:
        input.append(int(line))

# first sum
prev_sum = input[0] + input[1] + input[2]
counter = 0
for i, depth in enumerate(input[1:-1]):
    # sum of three neighbouring depths
    depth_sum = input[i] + input[i+1] + input[i+2]
    print(depth_sum, depth_sum > prev_sum)
    if depth_sum > prev_sum:
        counter += 1

    prev_sum = depth_sum

print(counter)