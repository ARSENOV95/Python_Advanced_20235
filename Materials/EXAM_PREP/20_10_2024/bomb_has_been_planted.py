DEFUSE_TIME = 4

def in_borders(r,c,mx_r,mx_c):
    return 0 <= r < mx_r and 0 <= c < mx_c

def movements(cmd,r,c,time):
    if cmd == 'up':
        r -= 1
    elif cmd == 'down':
        r += 1
    elif cmd == 'left':
        c -= 1
    elif cmd == 'right':   
        c += 1
 
    time -= 1   #each movement will cost as second might as well imput the logic in here 
    return r,c,time


rows,cols = map(int,input().split(', '))

matrix = []

row = col = 0

for i in range(rows):
    curr_row = [x for x in input()]
    if 'C' in curr_row:
        row = i
        col = curr_row.index('C')
    matrix.append(curr_row)

ct_r,ct_c = row,col
terrorists = 0
is_defusing = False

mission_time = 16 #seconds

while True:
    command = input()

    if mission_time <= 0:
        break

    if command != 'defuse':
        next_row,next_col,mission_time = movements(command,row,col,mission_time)

        if not in_borders(next_row,next_col,rows,cols):
            continue

        if matrix[next_row][next_col] == 'T':
            matrix[next_row][next_col] = '*'
            print('Terrorists win!')
            break

        elif matrix[next_row][next_col] in ('B','*'):
            row,col = next_row,next_col
    
    elif command == 'defuse':
        if matrix[row][col] == 'B':
            if mission_time - DEFUSE_TIME >= 0:
                matrix[row][col] =  matrix[row][col] = 'D'
                print("Counter-terrorist wins!")
                print(f"Bomb has been defused: {mission_time - DEFUSE_TIME} second/s remaining.")

            else: 
                matrix[row][col] = 'X'
                print('Terrorists win!')
                print("Bomb was not defused successfully!")
                print(f"Time needed: {abs(mission_time - DEFUSE_TIME)} second/s.")
            break
        
        elif  matrix[row][col] != 'B':
            mission_time -= 2
            if mission_time < 0:
                print('Terrorists win!')
                print("Bomb was not defused successfully!")
                print(f"Time needed: {0} second/s.")


          
                
        
     

[print(*row,sep='') for row in matrix]
 