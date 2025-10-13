def in_bounderies(r, c, size):
    return 0 <= r < size and 0 <= c < size


n = int(input())  # the filed is square

matrix = []
player_position = None

for index in range(n):
    curr_row = input().split()
    if 'P' in curr_row:
        player_position = (index, curr_row.index('P'))
    matrix.append(curr_row)

moves = {'up': lambda r, c: (r - 1, c),
         'down': lambda r, c: (r + 1, c),
         'left': lambda r, c: (r, c - 1),
         'right': lambda r, c: (r, c + 1),
         }

stars_count = 2

while True:
    if stars_count == 0:
        print("Game over! You are out of any stars.")
        break

    curr_row = player_position[0]
    curr_col = player_position[1]

    move = input()

    next_row, next_col = moves[move](curr_row, curr_col)

    if not in_bounderies(next_row, next_col, n):
        next_row,next_col = (0, 0)

    if matrix[next_row][next_col] != '#':
        if matrix[next_row][next_col] == '*':
            stars_count += 1

        matrix[next_row][next_col] = 'P'
        matrix[curr_row][curr_col] = '.'
        player_position = (next_row, next_col)

        if stars_count == 10:
            print("You won! You have collected 10 stars.")
            break

    elif matrix[next_row][next_col] == '#':
        stars_count -= 1
        continue

print(f"Your final position is [{player_position[0]}, {player_position[1]}]")

[print(*row, sep=' ') for row in matrix]