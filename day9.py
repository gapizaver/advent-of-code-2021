# Read input
heightmap = []
with open("input.txt") as file:
    for line in file:
        heightmap.append([int(x) for x in line.rstrip()])


sum_of_risk_levels = 0
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
        
        if higher_neighbors >= 4:
            sum_of_risk_levels += height + 1


print(sum_of_risk_levels)