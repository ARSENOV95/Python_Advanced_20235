matrix = [[int(x) for x in input().split(', ')] for _ in range(int(input()))]




flatten = [num for lst in matrix for num in lst]

print(flatten)