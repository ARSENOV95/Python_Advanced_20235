odd_set = set()
even_set = set()

num = int(input())

for i in range(1, num + 1):
    name = input()
    curr_name = sum(ord(ch) for ch in name) //i #deviding by the current row

    if curr_name % 2 == 0:
        even_set.add(curr_name)
    else:
        odd_set.add(curr_name)

odd = sum(odd_set)
even= sum(even_set)

if odd == even:
    result =  odd_set | even_set

elif odd > even:
    result = odd_set - even_set
else:
    result = odd_set ^ even_set

print(', '.join(str(x) for x in result))