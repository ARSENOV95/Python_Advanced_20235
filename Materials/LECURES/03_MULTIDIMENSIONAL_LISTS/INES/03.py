rows = int(input())

nums = []

for _ in range(rows):
    row_data = [int(el) for el in input().split(", ")]
    nums.extend(row_data) # direct unpacling of the row at the end of the list

print(nums)