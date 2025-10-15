def boundes(r,c,n):
    return 0 <= r < n and 0 <= c <= n

n = int(input())

gambler = (0,0)

board = []

for r_index in range(n):
    curr_row = list(input())
    if 'G' in curr_row:
        gambler = (r_index,curr_row.index('G'))
        curr_row[curr_row.index('G')] = '-'
    board.append(curr_row)

inital_pot = 100

moves = {"up": lambda r,c: (r - 1,c), 
         "down": lambda r,c: (r + 1,c),
         "left": lambda r,c: (r,c - 1),
         "right": lambda r,c: (r,c + 1),
        }

while (command := input()) != 'end':
    if inital_pot == 0:
        break

    curr_row,curr_col = gambler[0],gambler[1]

    move = input()

    next_row,next_col = moves[move](curr_row,curr_col)

    if not boundes(next_row,next_col,n):
        inital_pot = 0
        break

    board[next_row][next_col,n] = '-'
    gambler = (next_row,next_col,n)
    if board[next_row][next_col,n] == 'W':
        inital_pot += 100
    elif board[next_row][next_col,n] == 'P':
        inital_pot -= 200
    elif board[next_row][next_col,n] == 'J':
        inital_pot += 100000
        board[next_row][next_col,n] = 'G'
        print("You win the Jackpot!")
        break

    board[next_row][next_col,n] = 'G'


if inital_pot:
    print(f"End of the game. Total amount: {inital_pot}$")
    [print(*row,sep='') for row in board]
        
else:
    print("Game over! You lost everything!")

