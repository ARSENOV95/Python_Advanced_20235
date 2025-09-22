from collections import deque


# waht is a snake like pattern?

r,c = map(int,input().split())

matrix = []

string = deque(input())
# to crate an easier snake pattern we can use a deque so we can rotatete it

for row in range(r):
    matrix.append([""]* c)
    #first we create a rows fo the matrix with empy values
    for col in range(c): #after we create the roes for each row w loop troug h the columns
        if row % 2 == 0:
            #if the column is even we start filling from the  left to right 0,1,2,3,5...
            matrix[row][col] = string[0]
            #we fill the current index in rotation with the first evelemnt from the deque S and we move S to the back of the deque to get that snake pattern
        else:
            #if the row is odd, we will fill the row form the righ meaning -1 - col (0) = -1, ,-2,-3,-4,-5,
            matrix[row][- 1- col] = string[0]     

        string.rotate(-1)
        #we rotarte he deuqe = Softuni after first row = iSoftUn.. second row = niSoftU.. and so on 
[print(*row,sep ='') for row in matrix]



