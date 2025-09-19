n = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(n)]

primary_diagoinal = [matrix[i][i] for i in range(n)]
secondary_diagoinal = [matrix[i][ -1 - i] for i in range(n)]

print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagoinal)}. Sum: {sum(primary_diagoinal)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary_diagoinal)}. Sum: {sum(secondary_diagoinal)}")