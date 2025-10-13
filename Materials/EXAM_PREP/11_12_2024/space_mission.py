def in_space(r, c, n):
    return 0 <= r < n and 0 <= c < n


REFUEL_AMOUNT = 10
RESOURCE_PER_MOVE = 5

n = int(input())

ship_position = None  # locate inital ship postion
matrix = []  # vraible to store the grid layout

for index in range(n):
    current_row = input().split()
    if 'S' in current_row:
        ship_position = (index, current_row.index('S'))
    matrix.append(current_row)

initial_resources = 100

move_mapper = {'up': lambda r, c: (r - 1, c),
               'down': lambda r, c: (r + 1, c),
               'left': lambda r, c: (r, c - 1),
               'right': lambda r, c: (r, c + 1),
               }

while True:
    row = ship_position[0]
    col = ship_position[1]

    if initial_resources < 5:
        matrix[row][col] = 'S'
        print("Mission failed! The spaceship was stranded in space.")
        break
    
    move = input()


    new_row, new_col = move_mapper[move](row, col)
    initial_resources -= RESOURCE_PER_MOVE  # after locating the new postion the resource is taken to make the move
    if  matrix[row][col] != 'R':
        matrix[row][col]  = '.'
   

    if not in_space(new_row, new_col, n):
        matrix[row][col] = 'S'
        print("Mission failed! The spaceship was lost in space.")
        break

    if matrix[new_row][new_col] == 'M':
        initial_resources -= RESOURCE_PER_MOVE

    elif matrix[new_row][new_col] == 'R':
        initial_resources += REFUEL_AMOUNT
        if initial_resources > 100:
            initial_resources = 100
    elif matrix[new_row][new_col] == 'P':

        print(f"Mission accomplished! The spaceship reached Planet B with {initial_resources} resources left.")
        break

    ship_position = (new_row,new_col)   
    
        


    [print(*row, sep=' ') for row in matrix]

