from collections import deque

time_per_task = deque(int(x) for x in input().split())
number_of_tasks = [int(x) for x in input().split()]

rubber_ducks = {

}

collected_ducks = {'Darth Vader Ducky':0
                  ,'Thor Ducky':0
                  ,'Big Blue Rubber Ducky':0
                  ,'Small Yellow Rubber':0
                }

while time_per_task and number_of_tasks:
    curr_time = time_per_task[0]
    curr_task = number_of_tasks[-1]

    curr_duck = None

    task_time = curr_task * curr_time

    if task_time in range(0,240):
        if task_time in range(0,61):
            curr_duck = 'Darth Vader Ducky'
        elif task_time in range(61,121):
            curr_duck = 'Thor Ducky'
        elif task_time in range(121,181):    
            curr_duck = 'Big Blue Rubber Ducky'    
        elif task_time in range(181,241):  
            curr_duck = 'Small Yellow Rubber'   

        collected_ducks[curr_duck] += 1
        time_per_task.popleft()
        number_of_tasks.pop()

    else:
        number_of_tasks[-1] -= 2
        time_per_task.rotate(-1)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")

for duck,count_duck in collected_ducks.items():
    print(f'{duck}: {count_duck}')
