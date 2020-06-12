import numpy as np
##Doesnt work either.
def posVal():
    pass

def sudoku(puzzle):
    for x in range(9):
        for y in range(9):
            if(puzzle)

puzzle = [
            [5,3,0,  0,7,0,  0,0,0],
            [6,0,0,  1,9,5,  0,0,0],
            [0,9,8,  0,0,0,  0,6,0],

            [8,0,0,  0,6,0,  0,0,3],
            [4,0,0,  8,0,3,  0,0,1],
            [7,0,0,  0,2,0,  0,0,6],

            [0,6,0,  0,0,0,  2,8,0],
            [0,0,0,  4,1,9,  0,0,5],
            [0,0,0,  0,8,0,  0,7,9]   ]

print(np.matrix(puzzle))
sudoku(puzzle)
print(np.matrix(puzzle))

'''

x, y
f = 0
while(f!=10)
    for (x=0; x<=y; x++)
        y = x+f
        f++
        return x,y

            x,x
        x,x+1, x+1,x
    x,x+2, x+1,x+1, x+2,x
x,x+3, x+1,x+2, x+2,x+1, x+4,x
        x,x
    x,x+1, x+1,x
x,x+2, x+1,x+1, x+2,x

        1-1
       12-21
     13-22-31
    14-23-32-41
  15-24-33-42-51
16
17
18
19

29
38
47 ...
92

39
93

49
94

15-51

16-61

17-71

18-81

19-91

29-92

39-93

49-94

59-95

69-96

79-97

89-98

99-99

'''
