n, m = [int(x) for x in input().split(',')]

mouse = (0, 0)
cheese = 0

matrix = []

for r_idx in range(n):
    curr_row = list(input())
    if 'M' in curr_row:
        mouse = (r_idx, curr_row.index('M'))
    cheese += curr_row.count('C')
    matrix.append(curr_row)

moves = {"up": (-1, 0),
         "down": (1, 0),
         "left": (0, -1),
         "right": (0, 1)
         }

while True:
    c_row = mouse[0]
    c_col = mouse[1]

    command = input()

    if command == 'danger':
        print("Mouse will come back later!")
        break

    n_row = c_row + moves[command][0]
    n_col = c_row + moves[command][1]

    if not (0 <= n_row < n and 0 <= n_col < m):
        print("No more cheese for tonight!")
        break

    if matrix[n_row][n_col] == '@':
        continue

    matrix[c_row][c_col] = '*'

    if matrix[n_row][n_col] == 'C':
        matrix[n_row][n_col] = 'M'
        cheese -= 1
        if cheese <= 0:
            print("Happy mouse! All the cheese is eaten, good night!")
            break

    elif matrix[n_row][n_col] == 'T':
        matrix[n_row][n_col] = 'M'
        print("Mouse is trapped!")
        break

    mouse = (n_row, n_col)

[print(*row, sep='') for row in matrix]