def minor(comd :str,r :int,c :int,movements :dict,border):
    if 'left' in comd or 'right' in comd:
        c += movements[comd]
    elif 'up' in comd or 'down' in comd:
        r += movements[comd]

    return 0 <= r < border and  0 <= c < border


def coal_calculator(comd :str,r :int,c :int,movements :dict):
    if 'left' in comd or 'right' in comd:
        c = c + movements[comd]
    elif 'up' in comd or 'down' in comd:
        r = r + movements[comd]
    return r,c



n = int(input())

commands = input().split()


grid = []

minor_position = None
total_coal = 0
collected = 0

for row_idx in range(n):
    row_data = input().split()
    if 's' in row_data:
        position = row_data.index('s')
        minor_position = (row_idx,position)
    
    if 'c' in row_data:
        total_coal += 1

    grid.append(row_data)

#print(minor_position)

monor_movements = {'left': -1,'right':1,'up':-1,'down':1}

row,col = minor_position

for command in commands:
    if collected == total_coal:
        exit(f'You collected all coal! ({row},{col})')


    #print(row,col,'CURRENT POS BEFORE COMMAND',sep = ' ')
    if not minor(command,row,col,monor_movements,n):
        continue

    row,col = coal_calculator(command,row,col,monor_movements)

    if grid[row][col] == 'c':
       collected += 1
       grid[row][col] == '*'


    #print(row,col,'NEW POS AFTER COMMAND',sep = ' ')
    #print(collected)

    elif grid[row][col] == 'e':
        exit(print(f'Game over! ({row},{col})'))

    


else:
    print(f'{total_coal - collected} pieces of coal left. ({row},{col})')
    




    


  

    
