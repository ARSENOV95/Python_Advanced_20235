def minor(comd :str,r :int,c :int,movements :dict,border):
    if 'left' in comd or 'right' in comd:
        c += movements[comd]
    elif 'up' in comd or 'down' in comd:
        r += movements[comd]

    return 0 <= r < border and  0 <= c < border


def coal_calculator(comd :str,r :int,c :int,movements :dict,r1 :int, c1: int):
    if 'left' in comd or 'right' in comd:
        c1 = c + movements[comd]

    elif 'up' in comd or 'down' in comd:
        r1 = r + movements[comd]
    
    return r1,c1

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
                   
for command in commands:
    


    row,col = minor_position
    row_new = 0
    col_new = 0
    if not minor(command,row,col,monor_movements,n):
        continue

    row_new,col_new = coal_calculator(command,row,col,monor_movements,row_new,col_new)

    if grid[row_new][col_new] == 'c':
       collected += 1
       grid[row_new][col_new] == '*'
       row,col = row_new,col_new
    
    print(row_new,col_new)
    print(collected)

    #elif grid[row_new][col_new] == 'e':
    #    exit(print(f'Game over! {row_new},{col_new}'))

    #elif collected == total_coal:
    #    exit(f'You collected all coal! {row_new},{col_new}')



    




    


  

    
