class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # Perform folding along y axis
    def yfold(self, folding_line):
        if self.y > folding_line:
            self.y = 2*folding_line - self.y
    
    # Perform folding along x axis
    def xfold(self, folding_line):
        if self.x > folding_line:
            self.x = 2*folding_line - self.x

# Read input
points = []
with open("input.txt") as file:
    for line in file:
        if line.rstrip() != "":
            if "," in line:
                points.append(Point(
                    (int) (line.rstrip().split(",")[0]),
                    (int) (line.rstrip().split(",")[1])
                ))
            else:
                # Perform folding
                folding_line = (int) (line.rstrip().split()[2].split("=")[1])
                axis = line.rstrip().split()[2].split("=")[0]
                for point in points:
                    # Folding along y axis
                    if axis == "y":
                        point.yfold(folding_line)

                    # Folding along x axis
                    else:
                        point.xfold(folding_line)


# Put points' coordinates in set
visible_points_coordinates = set()
for point in points:
    visible_points_coordinates.add((point.x, point.y))

for i in range(100):
    for j in range (100):
        if (i, j) in visible_points_coordinates:
            print("x", end="")
        else:
            print(" ", end="")
    
    print()
