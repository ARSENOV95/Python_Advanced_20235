def  create_set_from_range(range_ :str)->set:
    start,end = [int(x) for x in range_.split(',')]
    return set(range(start,end+1))

longest_inersection = set()

for _ in range(int(input())):
    first_range,second_range = input().split('-')

    first_start,first_end = [int(x) for x in first_range.split(',')]
    second_start,second_end = [int(x) for x in  second_range.split(',')]

    first_set = create_set_from_range(first_range)
    second_set = create_set_from_range(second_range)

    current_intersection = first_set & second_set

    if current_intersection > longest_inersection:
        longest_inersection = current_intersection

print(f'Longest intersection is {list(longest_inersection)} with length {len(longest_inersection)}')