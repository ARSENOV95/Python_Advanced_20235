MATRIX_RANGE = 5

matrix = []

shooter = (0,0)

targets = 0

for r_idx in range(MATRIX_RANGE):
    curr_row = input().split()
    if 'A' in curr_row:
        shooter = (r_idx,curr_row.index('A'))
    targets += curr_row.count('x')

    matrix.append(curr_row)

commands = int(input())

targets_hit = 0

mover = {'up': lambda r,c,n: (r -n,c),
         'down': lambda r,c,n: (r + n,c),
         'left': lambda r,c,n: (r,c - n),
         'right': lambda r,c,n: (r,c + n)
}


for command in range(commands):
    curr_command = input().split()

    if curr_command[0] == 'move':
        direciton,steps = curr_command[1:]
        next_row,next_col = mover[direciton](shooter[0],shooter[1],steps)

        print(next_row,next_col)

        if matrix[next_row][next_col] == '.':
            matrix[shooter[0]][shooter[1]] = '.'
            matrix[next_row][next_col] == 'A'
            shooter(next_row,next_col)


    elif curr_command[0] == 'shoot':
        pass


