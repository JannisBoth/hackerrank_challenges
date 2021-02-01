import re

def nextMove(n,r,c,grid):
    for row_id, row in enumerate(grid):
        # Extract position of princess (p) from the grid
        if "p" in row:
            princess_row = row_id
            princess_column = re.search("p", row, flags = 0).start() # get the index of p in the string

    if c == princess_column:
        # Bot and princess are in the same column
        # Change the row of the bot
        if r < princess_row:
            return "DOWN"        
        elif r > princess_row:
            return "UP"

    # Otherwise change the column of the bot
    elif c < princess_column:
        return "RIGHT"
    else:
        return "LEFT"  

n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))