#matrix = [[0 for j in range(2)] for i in range(3)]
#print(matrix)

###list_flattening, weh truning a multi deimentional list into a single row list 

matrix = [[1, 2, 3], [4, 5, 6]]

flattened = [num for sublist in matrix for num in sublist]

print(flattened)