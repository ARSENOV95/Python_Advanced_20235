box_of_clothes = list(map(int,input().split()))

rack_capacity = int(input())

#hlper vairables to store the rack count we start fro mthe 1st rack os the init val will be one 
rack_count = 1 
sum_clothers = 0 #variable to store the clothes ot be fitter on the rack , we start from 0 since we dont have anythong put on the first rack

#we itterate trough the bpx of clothes 
while box_of_clothes:
    #we take the current item for mthe top and check if we add it to the rack will be larger than the capacity
    curr_item = box_of_clothes.pop()

    # if we surpass capacity we move trough the next rack
    if (sum_clothers + curr_item) > rack_capacity:
        rack_count += 1
        sum_clothers = 0

    #finally in all cases we add the clothes to the current rack
    sum_clothers += curr_item

print(rack_count)

