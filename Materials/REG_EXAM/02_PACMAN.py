def boundery_reset(r, c, n):
    if r == n:
        r = 0
    elif c == n:
        c = 0
    elif r < 0:
        r = n - 1
    elif c < 0:
        c = n - 1
    return r, c


GHOST_DAMAGE = 50

n = int(input())

matrix = []

pacman = (0,0)
stars = 0

for r_idx in range(n):
    curr_row = list(input())
    if 'P' in curr_row:
        pacman = (r_idx, curr_row.index('P'))
    stars += curr_row.count('*')
    matrix.append(curr_row)

freeze = False

inital_health = 100

mapper = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

while True:
    if stars == 0:
        print(f"Pacman wins! All the stars are collected.")
        break

    command = input()

    if command == 'end':
        if stars:
            print('Pacman failed to collect all the stars.')
        break

    c_row = pacman[0]
    c_col = pacman[1]

    n_row = c_row + mapper[command][0]
    n_col = c_col + mapper[command][1]

    n_row, n_col = boundery_reset(n_row, n_col, n)

    matrix[c_row][c_col] = '-'
    pacman = (n_row, n_col)

    if matrix[n_row][n_col] == '*':
        stars -= 1


    elif matrix[n_row][n_col] == 'F':
        freeze = True

    elif matrix[n_row][n_col] == 'G':
        if not freeze:
            inital_health -= GHOST_DAMAGE
            if inital_health <= 0:
                print(f"Game over! Pacman last coordinates [{n_row},{n_col}]")
                break
        freeze = False

matrix[pacman[0]][pacman[1]] = 'P'

print(f"Health: {inital_health}")

if stars:
    print(f"Uncollected stars: {stars}")

[print(*row,sep='') for row in matrix]