boards = []
numbers = []

# read input
with open("input.txt") as file:
    numbers = [int(i) for i in file.readline().rstrip().split(",")]
    file.readline()
    board1 = []
    for line in file:
        if line.rstrip() != "":
            board1.append([int(i) for i in line.rstrip().split()])
        else:
            boards.append(board1)
            board1 = []
    boards.append(board1)

# draw numbers
drawn_numbers = set()
winner_drawn = 0            # last drawn number
winner_boards = []          # boards that have won

for drawn in numbers:
    # draw number
    drawn_numbers.add(drawn)
    
    # check rows and columns of every board
    for board in boards:
        # if board already won continure
        if board in winner_boards:
            continue

        # check rows
        found = True
        for row in board:
            found = True            # number is found in set
            for number in row:
                if number not in drawn_numbers:
                    found = False
                    break 
            if found :
                # add board to winner boards
                winner_boards.append(board)
                winner_drawn = drawn
                break
        # if winner do not check columns
        if found:
            continue

        # check columns
        board_w = len(board[0])     # width of board
        board_h = len(board)        # height of board
        for i in range(board_w):
            found = True
            for j in range(board_h):
                if board[j][i] not in drawn_numbers:
                    found = False
                    break
            if found:
                # add board to winner boards
                winner_boards.append(board)
                winner_drawn = drawn
                break
    
    # check if all boards have won
    if len(boards) == len(winner_boards):
        break
print(len(boards))
print(len(winner_boards))
print(drawn)
# find the sum of all unmarked numbers in last winning board
sum_unmarked = 0
for row in winner_boards[-1]:
    for number in row:
        if number not in drawn_numbers:
            sum_unmarked += number

print("result", sum_unmarked * winner_drawn)