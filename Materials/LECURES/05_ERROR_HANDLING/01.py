####################################################
#          original
#################################################

numbers_list = int(input()).split(", ")  - #syntax  error - if missing bracket after split method and and reunded bracket afther the imput function
                                           # typer error enclosing the function inth an int will not convert the ittrable, use map or comprehension to transform it
result = 1 
for i in range(numbers_list): #typer error - we canot range troug a list, it must be int 
    number = numbers_list[i+1] #index error we are looling aht the next number, and after the Nth element in the list we will have index out fo range
    if number <= 5 #syntax error = missing :
        result *= number 
    elif 5 < number <= 10: result /= number 
print(total) #name error = the variablre total has not been defined 








####################################################
#          corrected
#################################################


numbers_list = [int(x) for x in input().split(", ")]

result = 1

for i in range(len(numbers_list)): 
    number = numbers_list[i] 
    if number <= 5:
         result *= number 
    elif 5 < number <= 10: 
        result /= number 
        
print(result)