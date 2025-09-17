def seq_gen(seq :str):
    return set(int(x) for x in seq.split())

a = seq_gen(input())
b = seq_gen(input())

for _ in range(int(input())):
    command = input().split()
    command_body = ' '.join(command[:2])
    numbers = set(int(x) for x in command[2:])

    if command_body.startswith("Add First"):
        a.update(numbers)

    elif command_body.startswith('Add Second'):    
        b.update(numbers)  

    elif command_body.startswith("Remove First"):
        a.difference_update(numbers)  
    
    elif command_body.startswith('Remove Second'):
        b.difference_update(numbers) 

    elif command_body == "Check Subset":
        print((a <= b) or (b <= a))

print(*sorted(list(a)), sep=", ")
print(*sorted(list(b)), sep=", ")
       
 