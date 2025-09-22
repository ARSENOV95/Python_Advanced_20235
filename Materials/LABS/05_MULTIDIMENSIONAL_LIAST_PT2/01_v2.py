matrix = [x.split() for x in input().split("|")]

flat_list = [el for i in range(len(matrix) -1,-1,-1) for el in matrix[i]]

print(*flat_list)
