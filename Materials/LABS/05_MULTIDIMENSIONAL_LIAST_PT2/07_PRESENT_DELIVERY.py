presents = int(input())

size = int(input())

matrix = []

satan_position = (0,0)
nice_kids = 0 #stores the total count fo nice kids

for i_idx in range(size):
    curr_row = input().split()
    if 'S' in curr_row:
        satan_position = (i_idx,curr_row.index('S'))
    nice_kids += curr_row.count('V')
    matrix.append(curr_row)

moves = {'up': lambda r,c: (r-1,c),
         'down': lambda r,c: (r+1,c),
         'left': lambda r,c: (r,c-1),
         'right': lambda r,c: (r,c+1)
        }

while (command := input()) != 'Christmas morning':
    c_row = satan_position[0]
    c_col = satan_position[1]

    if presents == 0:
        break

    next_row,next_col = moves[command](c_row,c_col)

    if (0 <= next_row < size and 0 <= next_col < size):
        continue

    satan_position = (next_row,next_col)

    if matrix[next_row][next_col]  == 'V':
        presents -= 1
        nice_kids += 1
    
    elif  matrix[next_row][next_col] == 'C':
        for direction in moves.keys():
            r,c = moves[direction](next_row,next_col)  # we use the mapper with the cookie positon as reference  - next_row,enxt_col
            if  not (0 <= r < size and 0 <= c < size):     #we check if the surrounding positon is withing the matrix rangr
                continue

            if matrix[r][c] in 'VX':
                presents -= 1

    matrix[c_row][c_col] = '-'
    matrix[next_row][next_col] = 'S'


print(nice_kids)