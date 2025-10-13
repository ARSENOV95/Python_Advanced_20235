MONSTER_DMG = 40 #units
HEAL = 15 #HP per potion 

def in_bounderies(r,c,n):
    return 0 <= r < n and 0 <= c < n


n = int(input())

initial_health = 100

player_movements = {'up':lambda r,c: (r-1,c),
                    'down':lambda r,c: (r+1,c),
                    'left':lambda r,c: (r,c-1),
                    'right':lambda r,c: (r,c+1),
                    }

maze = []

player_position = None

for index in range(n):
    curr_row = list(input())
    if 'P' in curr_row:
        player_position = (index,curr_row.index('P'))
    maze.append(curr_row)


row = player_position[0]
col = player_position[1]

while True:
    move = input()

    new_row,new_col = player_movements[move](row,col)

    if not in_bounderies(new_row,new_col,n):
        continue

    maze[row][col] = '-'   
    row,col = new_row,new_col 

    if maze[row][col] == 'X':
        maze[row][col] = 'P'
        print("Player escaped the maze. Danger passed!")
        break

    elif maze[row][col] == 'M':
        initial_health -= MONSTER_DMG
        if initial_health > 0:
            maze[row][col] == '-'

        else:
            maze[row][col] = 'P'
            initial_health = 0
            print("Player is dead. Maze over!")
            break
    elif maze[row][col] == 'H':
        initial_health += HEAL
        if initial_health > 100:
            initial_health = 100

print(f"Player's health: {initial_health} units")

[print(*row,sep = '') for row in maze]
