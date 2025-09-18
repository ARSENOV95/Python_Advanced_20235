rows,columns = [int(x) for x in input().split(',')]

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

sum_cols = []

for j in range((columns)):
    row_sum = 0
    for i in range(rows):
        row_sum += (matrix[i][j])
    sum_cols.append(row_sum)

print(*sum_cols,sep='\n')