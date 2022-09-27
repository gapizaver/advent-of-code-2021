# Read input
positions = []      # Crab horizontal positions
with open("input.txt") as file:
    positions = list(map(int, file.read().split(",")))

# Check how much fuel is required for every crab to move to position
def fuel_consumption_to_pos(target_position):
    fuel_consumption = 0
    
    for position in positions:
        fuel_consumption += abs(position - target_position)
    
    return fuel_consumption


# Go through all positions and find the one which
# requires the least fuel

# Current position which requires the least fuel
minimal_fuel_position = positions[0]
# Amount of fuel to move to minimal_fuel_position
minimal_fuel_amount = fuel_consumption_to_pos(positions[0])

for i in range(max(positions)):
    if fuel_consumption_to_pos(i) < minimal_fuel_amount:
        minimal_fuel_position = i
        minimal_fuel_amount = fuel_consumption_to_pos(i)

# Print solution
print(minimal_fuel_amount)
