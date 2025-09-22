matrix = [x.split() for x in input().split("|")]


flat_list = []

for i in range(len(matrix) -1,-1,-1):
    for el in matrix[i]:
        flat_list.append(int(el))

print(flat_list)