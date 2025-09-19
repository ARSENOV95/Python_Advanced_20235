dimensions = int(input())

matrix = [[int(x) for x in input().split(",")] for _ in range(dimensions)]

primary = []
secondary = []

reverse = dimensions - 1

for i in range(dimensions):
    primary.append(matrix[i][i])
    secondary.append(matrix[i][reverse - i])

print(f"Primary diagonal: {', '.join(str(x) for x in primary)}. Sum: {sum(primary)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary)}. Sum: {sum(secondary)}")