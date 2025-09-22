n = int(input())

matrix = [[int(el) for el in input().split(', ')] for _ in range(n)]

lst = [el for row in matrix for el in row]

print(lst)