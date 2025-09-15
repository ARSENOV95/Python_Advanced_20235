from collections import deque

occurance = tuple(input().split())

values =  deque([])

for value in occurance:
    if value not in values:
        values.append(value)

while values:
    val = values.popleft()
    print(f'{float(val):.1f} - {occurance.count(val)} times')

