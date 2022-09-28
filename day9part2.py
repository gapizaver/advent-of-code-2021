# Read input
import math


# Read input
heightmap = []
with open("input.txt") as file:
    for line in file:
        heightmap.append([int(x) for x in line.rstrip()])


# Find basin size, recursive function
checked_points = set()
def find_basin_size(x, y):
    # If height == 9 or already in set skip
    if heightmap[y][x] >= 9 or (x, y) in checked_points:
        return 0

    # Add point to already checked set
    checked_points.add((x, y))

    size = 1    # Add this point to the side
    # Check neighbors of the point
    if x > 0:
        size += find_basin_size(x-1, y)
    if x < len(heightmap[y]) - 1:
        size += find_basin_size(x+1, y)
    if y > 0:
        size += find_basin_size(x, y-1)
    if y < len(heightmap) - 1:
        size += find_basin_size(x, y+1)
    
    return size


# FInd low points
three_largest_basins = [0, 0, 0]
for i, row in enumerate(heightmap):
    for j, height in enumerate(row):
        higher_neighbors = 0 # Neighboring of the point that are higher

        if i > 0:
            if heightmap[i-1][j] > height:
                higher_neighbors += 1
        else:
            higher_neighbors += 1
        if i < len(heightmap) - 1:
            if heightmap[i+1][j] > height:
                higher_neighbors +=1
        else:
            higher_neighbors +=1
        if j > 0:
            if heightmap[i][j-1] > height:
                higher_neighbors += 1
        else:
            higher_neighbors +=1
        if j < len(heightmap[i]) - 1:
            if heightmap[i][j+1] > height:
                higher_neighbors +=1
        else:
            higher_neighbors +=1
        
        # Find basin size of the lowest point
        if higher_neighbors >= 4:
            # Checked points set can be reset
            checked_points = set()
            # Find basin size
            basin_size = find_basin_size(j, i)

            # Check if the basin among largest 3
            if min(three_largest_basins) < basin_size:
                three_largest_basins[three_largest_basins.index(min(three_largest_basins))] = basin_size


# Print solution
print(math.prod(three_largest_basins))
