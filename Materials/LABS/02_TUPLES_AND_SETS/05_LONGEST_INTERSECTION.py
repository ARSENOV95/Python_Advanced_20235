def create_sets(range_:str)->set:
    start,end = map(int,range_.split(','))
    return set(range(start,end+1))

intersection = set()

for _ in range(int(input())):
    ranges = input().split("-")

    set_1,set_2 = [create_sets(x) for x in ranges]

    if len(set_1 & set_2) > len(intersection):
       intersection =  set_1 & set_2

print(f'Longest intersection is {list(intersection)} with length {len(intersection)}')
