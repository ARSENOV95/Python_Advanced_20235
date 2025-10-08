TRIP_COST = 5
TOTAL_RESOURCES = 100
REFUEL = 10

def  movement_logic(move,r,c):
    if move == 'up':
        r -= 1
    elif move == 'down':
        r += 1
    elif move == 'left':
        c -= 1
    elif move == 'right':
        c += 1
    return r,c

def lost_in_space(r,c,size):
    return 0 <= r < size and 0 <= c < size

grid_size = int(input())

matrix = []

row = 0
col = 0

for i in range(grid_size):
    curr_row = input().split()
    if 'S' in curr_row:
        row = i
        col = curr_row.index('S')
    matrix.append(curr_row)

current_resource = TOTAL_RESOURCES

while True:
    command = input()

    if current_resource < 5:
        print("Mission failed! The spaceship was stranded in space.")
        break

    current_resource -= TRIP_COST

    next_row,next_col = movement_logic(command,row,col)

    if not lost_in_space(row,col,grid_size):
        print("Mission failed! The spaceship was lost in space.")
        break


    if matrix[next_row][next_col] == 'M':
        matrix[row][col]  = '.'
        current_resource -= TRIP_COST
        

    elif matrix[next_row][next_col] == 'R':
        refuel = min(REFUEL,(TOTAL_RESOURCES - current_resource))
        current_resource += refuel

    elif matrix[next_row][next_col] == 'P':
        print(f"Mission accomplished! The spaceship reached Planet B with {current_resource} resources left.")
        break

    row,col = next_row,next_col

    if matrix[row][col] != 'R':
        matrix[row][col] = 'S'

[print(*row) for row in matrix]
