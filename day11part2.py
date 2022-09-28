# Read input
dumbos = []     # Dumbo octopuses' energy levels
with open("input.txt") as file:
    for line in file:
        dumbos.append([int(x) for x in line.rstrip()])


# Dumbos that already flashed in the step
flashed_dumbos_in_step = set()
# Number of Dumbos' flashes
num_of_flashes = 0

# Flash Dumbo at position x,y
def flash(x, y):
    # Reset energy level
    dumbos[y][x] = 0
    # Increment flash counter
    global num_of_flashes
    num_of_flashes += 1

    # Increment energy of adjacent octopuses
    if y > 0:
        increment_energy(x, y-1)
        if x > 0:
            increment_energy(x-1,y-1)
        if x < len(dumbos[y]) - 1:
            increment_energy(x+1, y-1)
    if y < len(dumbos) - 1:
        increment_energy(x, y+1)
        if x > 0:
            increment_energy(x-1,y+1)
        if x < len(dumbos[y]) - 1:
            increment_energy(x+1, y+1)
    if x > 0:
        increment_energy(x-1,y)
    if x < len(dumbos[y]) - 1:
        increment_energy(x+1, y)


# Increment energy level of Dumbo at position x,y
def increment_energy(x, y):
    # Check if the Dumbo already flashed this step
    if (x, y) in flashed_dumbos_in_step:
        return

    # Increment energy
    dumbos[y][x] += 1

    # Dumbo flashes
    if dumbos[y][x] > 9:
        flashed_dumbos_in_step.add((x, y))
        flash(x, y)


# Find the first step at which all Dumbos flash
i = 1
while True:
    # Reset flashed_dumbos_in_step
    flashed_dumbos_in_step = set()

    # Increment energy level of every Dumbo
    for y, row in enumerate(dumbos):
        for x, dumbo in enumerate(row):
            increment_energy(x, y)
    
    if len(flashed_dumbos_in_step) == len(dumbos) * len(dumbos[1]):
        print("First step during which all Dumbos flash:", i)
        break
    
    i += 1
