n = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(n)]


if len(matrix) > 0:
    coordinates = []
    for pair in input().split():
        x,y = map(int,pair.split(","))
        coordinates.append([x,y])
    
    

    for coordinate in coordinates:
        row,col = coordinate

        if 0 < row < n -1:
            r_start,r_end = row - 1,row + 2
            if 0 < col < n -1:
                c_start,c_end = col - 1,col + 2
            elif col == 0:
                c_start,c_end = col,col + 2
            elif col == n-1:
                c_start,c_end = col -1,col + 1
    
        elif row == 0:
            r_start,r_end = row,row + 2
            if 0 < col < n -1:
                c_start,c_end = col - 1,col + 2

            elif col == 0:  
                c_start,c_end = col,col + 2
            else:
                c_start,c_end = col -1,col + 1

        elif row == n-1:
            r_start,r_end = row -1,row + 1
            if 0 < col < n -1:
                c_start,c_end = col - 1,col + 2

            elif col == 0:  
                c_start,c_end = col,col + 2
            elif col == n- 1:
                c_start,c_end = col -1,col + 1

        if matrix[row][col] > 0:
            val = matrix[row][col]
        else:
            continue

        for r in range(r_start,r_end):
           for c in range(c_start,c_end):
               if matrix[r][c] > 0:
                    matrix[r][c] -= val


alive_cells = [i for row in matrix for i in row if i > 0]

print(f'Alive cells: {len(alive_cells)}')
print(f'Sum: {sum(alive_cells)}')

[print(*row) for row in matrix]