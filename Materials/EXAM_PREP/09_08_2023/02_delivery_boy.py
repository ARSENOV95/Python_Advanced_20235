def deliver_in_time(r, c, n, m):
    return 0 <= r < n and 0 <= c < m


row, col = [int(x) for x in input().split()]

matrix = []

delivery_boy = (0, 0)


mapper = {'up': (-1,0), 'down': (1,0), 'left': (0,-1), 'right': (0,1)}

for r_index in range(row):
    curr_row = list(input())
    if 'B' in curr_row:
        delivery_boy = (r_index,curr_row.index('B'))
    matrix.append(curr_row)

curr_position = delivery_boy

while True:
    curr_row, curr_col = curr_position

    command = input()

    next_row,next_col = curr_row + mapper[command][0], curr_col + mapper[command][1]

    if not deliver_in_time(next_row, next_col, row, col):
        print("The delivery is late. Order is canceled.")
        matrix[delivery_boy[0]][delivery_boy[1]] = ' '
        break

    if matrix[next_row][next_col] == '*':
        continue

    curr_row,curr_col = next_row,next_col

    if matrix[curr_row][curr_col] == '-':
        matrix[curr_col][curr_col] = '.'

    elif matrix[curr_row][curr_col] == 'P':
         print("Pizza is collected. 10 minutes for delivery.")
         matrix[curr_row][curr_col] = 'R'

    elif matrix[curr_row][curr_col] == 'A':
         print("Pizza is delivered on time! Next order...")
         matrix[curr_row][curr_col] = 'P'
         break

    curr_position = next_row, next_col

[print(*row,sep ='') for row in matrix]



