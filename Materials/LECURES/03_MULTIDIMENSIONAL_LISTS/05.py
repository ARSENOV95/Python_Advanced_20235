
matrix = [[int(x) for x in input().split()] for _ in range(int(input()))]
#generates a 2D matrix with dimensions X by X where x is an interger input by the user

diagonal_sum = 0

for i in range(len(matrix)):
    diagonal_sum += (matrix[i][i])
    
print(diagonal_sum)

#took a while, to get every tiem diagoanly form a matrix you need to think as if its a grid for every itteraton you should take the index of the nested list and the the ndex matching the index of the nested list
# 
# how this looks, suppose the meatrix is 
# [[11,2,4],[4 5 6],[10,8,-12]] to take teh diag sum you need to loop trough each element 
# first loop - [11,2,4], and we take the first value 11, this will look like matrix[0][0]
# second will be [4 5 6] and we take the seconf value 5, matrix[1][1] - index 1,1 value of both val of the loop and nested value 
# third - [10,8,-12], we take the seconf value -12, matrix[2][2] - index 2,2 we are woriking with indexes so the max index will be len(matrix) - 1



