def fill_the_box(width,lenght,hight,*args):
    volume = width * lenght * hight

    boxes = 0

    for box in args:
        if box == 'Finish':
            break
        
        boxes += box

    if volume > boxes:
        return (f"There is free space in the box. You could put {volume - boxes} more cubes.")
    return (f"No more free space! You have {boxes - volume} more cubes.")

print(fill_the_box(2, 8,2, 2, 1, 7, 3, 1, 5,"Finish"))

print(fill_the_box(5, 5,2, 40, 11, 7, 3, 1, 5,"Finish"))