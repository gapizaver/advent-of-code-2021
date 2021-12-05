from typing import Counter


class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
    
    def vertical(self):
        return self.x1 == self.x2

    def horizontal(self):
        return self.y1 == self.y2


lines = []          # list of Lines
w = 0               # width of the diagram
h = 0               # height of the diagram
with open("input.txt") as file:
    for file_line in file:
        # coordinates of the line
        coor = [i.split(",") for i in file_line.rstrip().split(" -> ")]
        x1 = int(coor[0][0])
        y1 = int(coor[0][1])
        x2 = int(coor[1][0])
        y2 = int(coor[1][1])
        lines.append(Line(x1, y1, x2, y2))

        # change w and h if line bigger
        if x1 > w:
            w = x1
        if x2 > w:
            w = x2
        if y1 > h:
            h = y1
        if y2 > h:
            h = y2

# diagram init
diagram = []
for i in range(h+1):
    diagram.append([])
    for j in range(w+1):
        diagram[i].append(0)

# add points to diagram
for line in lines:
    # vertical lines
    if line.vertical():
        x = line.x1
        y1 = min(line.y1, line.y2)
        y2 = max(line.y1, line.y2)
        for i in range(y1, y2+1):
            diagram[i][x] += 1

    # horizontal lines
    elif line.horizontal():
        y = line.y1
        x1 = min(line.x1, line.x2)
        x2 = max(line.x1, line.x2)
        for i in range(x1, x2+1):
            diagram[y][i] += 1

# count values > 2 in diagram
counter = 0
for r in diagram:
    for val in r:
        if val >= 2:
            counter += 1

print("result", counter)


