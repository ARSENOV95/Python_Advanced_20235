def coordinate_validator(r :int,c :int,dim :int)->bool:
    return 0<= r < n and 0 <= c < n

n = int(input())

matrix = [[int(x) for x in input().split()] for i in range(n)]

#print(matrix)

while True:
    command = input()

    if command == 'END':
        [print(*row) for row in matrix]
        break

    body = command.split()

    row,col,val = map(int,body[1:])

    if not coordinate_validator(row,col,n):
        print("Invalid coordinates")
        continue

    if body[0] == 'Add':
        matrix[row][col] += val
    elif body[0] == 'Subtract':
        matrix[row][col] -= val

    