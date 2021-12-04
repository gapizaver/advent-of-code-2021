input = []

with open("input.txt") as file:
    for line in file:
        input.append(line.rstrip().split())

horizontal_pos = 0
depth = 0
aim = 0

for cmd in input:
    if cmd[0] == "forward":
        horizontal_pos += int(cmd[1])
        depth += aim*int(cmd[1])
    elif cmd[0] == "down":
        aim += int(cmd[1])
    elif cmd[0] == "up":
        aim -= int(cmd[1])

print("result:", depth*horizontal_pos)