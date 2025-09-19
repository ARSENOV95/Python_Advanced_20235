rows,columns = list(map(int,input().split(", ")))

matrix = [[int(x) for x in input().split(", ")] for _ in range(rows)]

square = []
max_sum = 0

for i in range(rows -1):
    for j in range(columns -1):
        row_1 = [matrix[i][j],matrix[i][j + 1]]
        row_2 = [matrix[i + 1][j],matrix[i + 1][j + 1]]
        square_sum = sum(row_1)  + sum(row_2)

        if  square_sum > max_sum:
            square = [row_1,row_2]
            max_sum =  square_sum

for i in square:
    print(f'{i[0]} {i[1]}')

print(max_sum)