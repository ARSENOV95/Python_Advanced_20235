from collections import deque as dq

players = dq(input().split())
safe = []

toss = int(input())

turn = 0

while len(players) > 1:  
    turn += 1

    curr_player = players.popleft()

    if turn == toss:
        print(f'Removed {curr_player}')
        turn = 0
        continue

    players.append(curr_player)

print(f'Last is {players[0]}')








    


