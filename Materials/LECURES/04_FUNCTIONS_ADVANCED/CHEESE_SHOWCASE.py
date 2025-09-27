def sorting_cheeses(**kwargs): # we pack the input into a dictionary
    sorted_cheeses = sorted(kwargs.items(),key = lambda kvp: (-len(kvp[1]), kvp[0])) #based on the condition we first sort by num of peices len of the lsit, and then alphabetical i f identical in pieces
    result = ''
    for cheese,quantities in sorted_cheeses: # for evert tuple in the  sorted list
        result += cheese + '\n' # for the outer loop we append cheese + \n so that in every itteration of the innter loop every val will be pritned o na new row, we do the same for the quntites
        for quantitny in sorted(quantities, reverse= True): #since they want us to print in reveres order we sort the list of qunities with reveres = True
            result += str(quantitny) + '\n'
    return result



print(
sorting_cheeses(
Parmesan=[102, 120, 135],
Camembert=[100, 100, 105, 500, 430],
Mozzarella=[50, 125],)
)
    
