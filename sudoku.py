import numpy as np

def possVal(j, i, k):
    global puzzle
    for r in range(9):
        if(puzzle[j][r] == k):return False

    for c in range(9):
        if(puzzle[c][i] == k):return False

    x0 = i//3
    y0 = j//3

    for y in range(3):
        for x in range(3):
            if(puzzle[y+y0][x+x0]==k):return False

    return True

def solve(j, i, k):
    global puzzle
    for k in range(1,10):
        if(possVal(j, i, k)):
            puzzle[j][i] = k

def sudoku():
    global puzzle
    for j in range(9):
        for i in range(9):
            if(puzzle[j][i]==0):
                solve(j, i, k)
                sudoku()

puzzle = [  [5,3,0,  0,7,0,  0,0,0],
            [6,0,0,  1,9,5,  0,0,0],
            [0,9,8,  0,0,0,  0,6,0],

            [8,0,0,  0,6,0,  0,0,3],
            [4,0,0,  8,0,3,  0,0,1],
            [7,0,0,  0,2,0,  0,0,6],

            [0,6,0,  0,0,0,  2,8,0],
            [0,0,0,  4,1,9,  0,0,5],
            [0,0,0,  0,8,0,  0,7,9]  ]

print(np.matrix(puzzle))

print("\n\n")

print(np.matrix(puzzle))
