rows = int(input())

diagonal_sum = 0

matrix = [[int(el) for el in input().split()] for _ in range(rows)]

for row_index in range(rows):
    diagonal_sum + (matrix[row_index][-1 - row_index])

print(diagonal_sum)