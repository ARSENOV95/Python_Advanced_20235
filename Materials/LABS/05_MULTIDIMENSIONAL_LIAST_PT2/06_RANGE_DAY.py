MATRIX_RANGE = 5

matrix = []

shooter = (0, 0)
targets = 0

for r_idx in range(MATRIX_RANGE):
    curr_row = input().split()
    if 'A' in curr_row:
        shooter = (r_idx, curr_row.index('A'))
    targets += curr_row.count('x')

    matrix.append(curr_row)

print(shooter)

commands = int(input())

targets_hit = []

mover = {'up': lambda r, c, n: (r - n, c),
         'down': lambda r, c, n: (r + n, c),
         'left': lambda r, c, n: (r, c - n),
         'right': lambda r, c, n: (r, c + n)
         }

for command in range(commands):
    curr_command = input().split()
    order, direction, = curr_command[0:2]
    if order == 'move':
        steps = curr_command[-1]

        next_row, next_col = mover[direction](shooter[0], shooter[1], int(steps))

        print(next_row, next_col)

        if not (0 <= next_row < MATRIX_RANGE and 0 <= next_col < MATRIX_RANGE):
            continue

        if matrix[next_row][next_col] == '.':
            matrix[shooter[0]][shooter[1]] = '.'
            matrix[next_row][next_col] = 'A'
            shooter = (next_row, next_col)

    elif order == 'shoot':
        n = 1 
        next_row,next_col = mover[direction](shooter[0], shooter[1],n)    

        while 0 <= next_row < MATRIX_RANGE and 0 <= next_col < MATRIX_RANGE:
            if matrix[next_row][next_col] == 'x':
                targets_hit.append([next_row, next_col])
                break

            n += 1    
            next_row,next_col = mover[direction](shooter[0], shooter[1],n)    
            
print(*targets_hit)