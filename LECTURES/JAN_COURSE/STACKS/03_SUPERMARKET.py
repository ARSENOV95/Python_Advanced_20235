from collections import deque

queue = deque([])

while (command := input()) !=  "End":
    queue.append(command)

for cus in queue:

    if cus == 'Paid':
       queue.popleft()
       break
    
    else:
       queue.popleft()
 

print(f"{len(queue)} people remaining.")