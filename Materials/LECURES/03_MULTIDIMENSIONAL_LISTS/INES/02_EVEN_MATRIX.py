row = int(input())

matrix = []

for i in range(row):
    row_date = [int(el) for el in input().split(", ") if int(el) %2 == 0]
    matrix.append(row_date)

print(matrix)