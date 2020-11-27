# to check if the selected path valid path (not 0 (wall), and the path hasn't been travelled yet)
def isValidPath(maze, row, col, solutions):
    if (maze[row][col] != 0) and \
            ((row >= 0 and row < len(maze)) and (col >= 0 and col < len(maze[0])) ) and \
            solutions[row][col] == 0:
        return True
    else:
        return False

# move the row and column given the direction
def move(row, col, dir):
    newrow = row
    newcol = col
    if dir == "up":
        newrow -= 1
    elif dir == "down":
        newrow += 1
    elif dir == "left":
        newcol -= 1
    elif dir == "right":
        newcol += 1
    return newrow, newcol

# solve the maze
def solveMaze(maze, row, col, solutions):
    # directions
    arah = ["up","down","left","right"]

    # check if our position is at the goal
    if maze[row][col] == 2:
        solutions[row][col] = 2
        return True

    # if we havent reached the goal yet
    else:
        # if we havent reached the goal yet
        solutions[row][col] = 1
        for dir in arah:
            # we move to another cell
            newrow, newcol = move(row, col, dir)
            # check if path taken is valid
            if isValidPath(maze, newrow, newcol, solutions):
                oldrow, oldcol = row, col
                row, col = newrow, newcol
                if solveMaze(maze, row, col, solutions):
                    return True
                else:
                    solutions[row][col] = 0
                    row, col = oldrow, oldcol
    return False


def print_maze(maze):
    for i in range(len(maze)):
        for j in maze[i]:
            print(j, end=" ")
        print()

# main function to test the maze solver
if __name__ == '__main__':

    maze = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [1,1,1,1,1,1,0,1,1,1,1,1,1,1,2],
            [0,1,0,0,0,1,0,1,0,0,0,0,0,0,0],
            [0,1,0,1,0,1,0,1,1,1,1,1,1,1,0],
            [0,1,0,1,0,1,0,0,0,1,0,1,0,0,0],
            [0,1,0,1,1,1,1,1,0,1,0,1,0,1,0],
            [0,1,0,1,0,0,0,1,0,0,0,1,0,1,0],
            [0,1,0,1,0,1,1,1,0,1,1,1,0,1,0],
            [0,1,0,1,0,1,0,0,0,1,0,0,0,1,0],
            [0,1,0,1,0,1,0,1,1,1,0,1,1,1,0],
            [0,1,0,1,0,1,0,1,0,0,0,1,0,1,0],
            [0,1,0,1,0,1,1,1,1,1,1,1,0,1,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

    start_row = 1
    start_col = 0
    solutions = [[0 for a in range(len(maze[0]))] for b in range(len(maze))]

    print("\nis this maze solvable? = ", solveMaze(maze, start_row, start_col, solutions))
    print_maze(solutions)
