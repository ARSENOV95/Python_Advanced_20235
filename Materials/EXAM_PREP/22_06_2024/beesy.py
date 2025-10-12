MINIMUM_NECTAR = 30

def in_range(r,c,n):
    return 0<= r < n and 9 <= c < n

def new_position(r,c,n):
    if  r == n:
        r = 0
    elif r < 0:
        r = n - 1
    elif c == n:
        c = 0
    elif c < 0:
        c = n - 1
    return r,c
    

matrix_size = int(input())

starting_energy = 15

collected_nectar = 0

matrix = []

bonus_lives = 1 


r=c= 0 #bee coordinates 

for i in range(matrix_size):
    current_row = list(input())
    if 'B' in current_row:
        r = i
        c = current_row.index('B')
    matrix.append(current_row)


moves = {"up": lambda r,c: (r - 1,c), 
         "down": lambda r,c: (r + 1,c), 
         "left": lambda r,c: (r,c - 1),  
         "right": lambda r,c: (r,c + 1)
        }

while starting_energy > 0:
    cmd = input()

    nr,nc = moves[cmd](r,c)
    matrix[r][c] = '-'

    if not in_range(nr,nc,matrix_size):
        nr,nc = new_position(nr,nc,matrix_size)

    starting_energy -= 1   

    if matrix[nr][nc].isdigit():
        collected_nectar += int(matrix[nr][nc])
       
    elif matrix[nr][nc] == 'H':
        
        if collected_nectar >= MINIMUM_NECTAR:
            print(f"Great job, Beesy! The hive is full. Energy left: {starting_energy}")
        else:
            print("Beesy did not manage to collect enough nectar.")

        break

    if starting_energy == 0:
        if collected_nectar > 30 and bonus_lives != 0:
            starting_energy += (collected_nectar - MINIMUM_NECTAR)
            bonus_lives = 0 
        else:
            print('This is the end! Beesy ran out of energy.')
            break

    r,c = nr,nc

matrix[nr][nc] = 'B'
[print(*row,sep ='') for row in matrix]




