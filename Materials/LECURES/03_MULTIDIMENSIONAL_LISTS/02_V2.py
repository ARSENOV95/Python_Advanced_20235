print([[int(x) for x in input().split(", ") if int(x) %2 == 0] for _ in range(int(input()))])

#a pretty cheeky list comprehesion 

#from left to right for every itteraiton of the loop for the given range N
#we take as imput the output of the nested loop looptgn trough each item of a created list, the reuslt will eb a nester list
