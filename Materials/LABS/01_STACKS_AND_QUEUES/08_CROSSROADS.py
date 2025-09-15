from collections import deque

light_duration_init = int(input())
free_window = int(input())

interal = light_duration_init
free = free_window

cars = deque([])

cars_in_queue = 0
cars_passed = 0

while (make := input()) != 'END':
    cars.append(make)
    if make != 'green':
        cars_in_queue += 1


while cars_in_queue:

    curr_make = cars.popleft()

    if curr_make != 'green':
        cars_in_queue -= 1


        if len(curr_make) <= interal:
            interal -= len(curr_make)

        elif len(curr_make) > interal and abs(interal - len(curr_make)) <= free:
            interal = 0
            free -= abs(interal - len(curr_make))

        else:
            hit =  free - len(curr_make) 
            print('A crash happened!')
            print(f'{curr_make} was hit at {curr_make[::hit]}')
            break

        cars_passed += 1
    
    else:
        interal = light_duration_init
        free  = free_window

else:
    print('Everyone is safe.')
    print(f'{cars_passed} total cars passed the crossroads.')

