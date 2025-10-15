FISH_QUOTA = 20

def area_left(r,c,n):
    if r < 0:
        r = n -1
    elif r == n:
        r = 0
    elif c < 0:
        c = n - 1
    elif c == n:
        c = 0
    else:
        return r,c
    return r,c


size = int(input())

matrix = []

fisherman = (0,0)

for r_index in range(size):
    curr_row = list(input())
    if 'S' in curr_row:
        fisherman = (r_index,curr_row.index('S'))
    matrix.append(curr_row)

fish_cought = 0

moves = {"up":(-1,0), "down":(+1,0), "left":(0,-1),"right":(0,1)}

is_whirlpool = False


while (command:=input()) != 'collect the nets':
    curr_row,curr_col = fisherman

    next_row = curr_row + moves[command][0]
    next_col = curr_col + moves[command][1]

    next_row,next_col =  area_left(next_row,next_col,size)


    if matrix[next_row][next_col] == 'W':
        is_whirlpool = True
        break

    elif matrix[next_row][next_col].isdigit():
        fish_cought += int(matrix[next_row][next_col])

    matrix[curr_row][curr_col] = '-'   
    matrix[next_row][next_col] = 'S'
    fisherman = (next_row,next_col)
    

if is_whirlpool:
   print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [{curr_row},{curr_col}]")

else:
    if fish_cought >= FISH_QUOTA:
        print("Success! You managed to reach the quota!")
    else:
        print(f"You didn't catch enough fish and didn't reach the quota! You need {FISH_QUOTA - fish_cought} tons of fish more.")

    if fish_cought:
        print(f"Amount of fish caught: {fish_cought} tons.")

    [print(*row,sep='') for row in matrix]

