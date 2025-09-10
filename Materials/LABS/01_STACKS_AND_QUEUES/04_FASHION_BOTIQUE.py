box_of_clothes = list(map(int,input().split()))

rack_capacity = int(input())

rack_count = 1 
sum_clothers = 0

while box_of_clothes:
    curr_item = box_of_clothes.pop()

    if (sum_clothers + curr_item) > rack_capacity:
        rack_count += 1
        sum_clothers = 0

    sum_clothers += curr_item

print(rack_count)

