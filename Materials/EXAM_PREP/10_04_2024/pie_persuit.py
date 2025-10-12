from collections import deque

contestants = deque(int(x) for x in input().split())  #FIFO
pies = [int(x) for x in input().split()]   #LIFO

while contestants and pies:
    contestant = contestants[0]
    pie = pies[-1]

    result = contestant - pie
    
    if result > 0:
        contestants[0] -= pies.pop()
        contestants.rotate(-1)

    elif result == 0:
        contestants.popleft()
        pies.pop()
    else:
        pies[-1] = abs(result)
        if pies[-1] == 1 and len(pies) > 1:
            lefover = pies.pop()
            pies[-1] += lefover

        contestants.popleft()

if not pies and contestants:
    print("We will have to wait for more pies to be baked!")
    print(f'Contestants left: {", ".join(str(x) for x in contestants)}')

elif not contestants and pies:
    print("Our contestants need to rest!")
    print(f'Pies left: {", ".join(str(x) for x in pies)}')

else:
    print('We have a champion!')