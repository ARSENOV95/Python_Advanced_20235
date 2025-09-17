from collections import deque

operations = {"+": lambda a,b: a + b,
              "*": lambda a,b: a * b,
              "-": lambda a,b: a - b,
              "/": lambda a,b: a // b if b != 0 else 0,         
            }

symbols = input().split()


numbers = deque([])

for char in symbols:
    if char not in '*,+,-,/':
        numbers.append(int(char))

    else:
        while len(numbers) > 1:
            fist = numbers.popleft()
            second = numbers.popleft()
            numbers.appendleft(operations[char](fist,second))

print(*numbers)