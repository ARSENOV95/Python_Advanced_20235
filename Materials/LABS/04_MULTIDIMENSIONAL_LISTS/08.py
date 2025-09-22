n = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(n)]

coordinates = []

for pair in input().split():
    x,y = map(int,pair.split(","))
    coordinates.append([x,y])

for coordinate in coordinates:
    row,col = coordinate

    if  0 <= row -1 < n and row < row + 1 < n and 0 <= col -1 < n and col <= col + 1 < n: 
        r_start,r_end = row - 1,row + 2
        c_start,c_end = col - 1,col + 2

    elif 0 <= row -1 < n and row < row + 1 < n and 0 > col -1:
        r_start,r_end = row - 1,row + 2
        c_start,c_end = col,col + 2
    elif 0 <= row -1 < n and row < row + 1 < n and  col == n:
        r_start,r_end = row - 1,row + 2
        c_start,c_end = col -1,col + 1
    elif 0 > row -1:
        r_start,r_end = row,row + 2
        if col == n-1:
            c_start,c_end = col -1,col + 1
        elif 0 > col - 1:
            c_start,c_end = col,col + 2
    elif row + 1 == n:     
        r_start,r_end = row,row + 2
        if col == n -1:
            c_start,c_end = col -1,col + 1
        elif 0 > col - 1:
            c_start,c_end = col,col + 2
#
    val = matrix[row][col]

    for r in range(r_start,r_end):
       for c in range(c_start,c_end):
           if matrix[r][c] > 0:
                matrix[r][c] -= val
            


[print(*row) for row in matrix]