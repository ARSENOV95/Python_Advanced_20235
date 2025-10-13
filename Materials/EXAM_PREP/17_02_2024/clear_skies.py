ENEMY_DAMANGE = 0

n = int(input())

airspace = []

enemy_jets = 0
jet_position = None

for r_index in range(n):
    curr_row = list(input())
    if 'J' in curr_row:
        jet_position = (r_index,curr_row.index('J'))
    
    enemy_jets += curr_row.count('E')
    airspace.append(curr_row)

initial_armour = 300

directions = {
              'up': lambda r,c: (r-1,c), 
              'down': lambda r,c: (r+1,c), 
              'left': lambda r,c: (r,c -1),
              'right': lambda r,c: (r,c+ 1)
             }

while enemy_jets > 0:
    curr_row,curr_col = jet_position[0],jet_position[1]

    if initial_armour <= 0:
         print(f"Mission failed, your jetfighter was shot down! Last coordinates [{curr_row}, {curr_col}]!")
         break
    


    move = input()

    next_row,next_cow = directions[move](curr_row,curr_col)

    if airspace[next_row][next_cow] == 'E':
            initial_armour -= ENEMY_DAMANGE
            enemy_jets -= 1

    elif airspace[next_row][next_cow] == 'R':
        initial_armour = 300

    airspace[curr_row][curr_col] = '-'
    jet_position = (next_row,next_cow)


    if enemy_jets == 0:
         print('Mission accomplished, you neutralized the aerial threat!')


[print(*row,sep='') for row in airspace]
