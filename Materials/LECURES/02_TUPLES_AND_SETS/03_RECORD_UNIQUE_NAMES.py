num_names = int(input())

unique_names = set()

for name in range(num_names):
    curr_name = input()
    unique_names.add(curr_name)

for name in unique_names:
    print(name)