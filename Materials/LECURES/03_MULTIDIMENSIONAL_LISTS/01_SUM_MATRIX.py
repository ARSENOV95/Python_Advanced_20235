rows,columns = [int(x) for x in input().split(", ")]

sum_elements = 0

matrix = []

for i in range(rows):
    matrix.append([int(x) for x in input().split(", ")])
    sum_elements += sum(matrix[i])

print(sum_elements)
print(matrix)