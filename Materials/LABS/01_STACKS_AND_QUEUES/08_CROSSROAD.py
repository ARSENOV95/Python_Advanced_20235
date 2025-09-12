from collections import deque as dq

light_duration = int(input())
free_window_duration = int(input())

time_frame = light_duration + free_window_duration
curr_green = True


line_of_cars = dq([])
cars_passed = 0

while (make:= input()) != 'END':
    line_of_cars.appendleft(make)


while line_of_cars:

    curr_car = line_of_cars.popleft()

    if curr_car == 'green':
        time_frame = light_duration + free_window_duration
        continue

    else:
        if len(curr_car) > light_duration:
            curr_green = False

        time_frame -= len(curr_car)     

        if time_frame >= 0 and curr_green:
            cars_passed += 1

        else:
            print('A crash happened')
            print(F"{curr_car} was hit at {curr_car[time_frame]}.")
            break

else:
    print("Everyone is safe.")
    print(f"{cars_passed} total cars passed the crossroads.")