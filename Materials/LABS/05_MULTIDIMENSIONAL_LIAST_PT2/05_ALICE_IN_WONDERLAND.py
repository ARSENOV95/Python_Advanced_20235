NEEDED_TEA = 10

def range_checker(r,c,size):
    return 0 <= r < size and 0 <= c < n


n = int(input())


matrix = []
alice = ()

for r_idx in range(n):
    current_row  = input().split()
    if 'A' in current_row:
        alice = (r_idx,current_row.index('A'))
    matrix.append(current_row)

matrix[alice[0]][alice[1]] = '*'


tea = 0 

moves = {'up':(-1,0),
         'down':(1,0),
         'left':(0,-1),
         'right':(0,1)
         }

while True:

    move = input()

    next_row = alice[0] + moves[move][0]
    next_col = alice[1] + moves[move][1]


    if not range_checker(next_row,next_col,n):
        break
    
    alice = (next_row,next_col)

    if matrix[next_row][next_col].isdigit():
        tea += int(matrix[next_row][next_col])
        matrix[next_row][next_col] = '*'
        if tea >= NEEDED_TEA:
            break

    elif matrix[next_row][next_col] == 'R':
        matrix[next_row][next_col] = '*'
        break

    else:
        matrix[next_row][next_col] = '*'
    

if tea >= NEEDED_TEA:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

[print(*row,sep= ' ') for row in matrix]