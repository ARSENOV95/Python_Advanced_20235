n = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(n)]

primary_diagoinal = [matrix[i][i] for i in range(n)]
secondary_diagoinal = [matrix[i][ -1 - i] for i in range(n)]

print(sum(primary_diagoinal) - sum(secondary_diagoinal))
