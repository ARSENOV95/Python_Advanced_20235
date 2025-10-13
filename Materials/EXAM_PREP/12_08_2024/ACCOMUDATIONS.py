def accommodate(*groups,**rooms):
    accommodated = {}
    tot_accommodate = 0

    rooms = sorted(rooms.items(),key = lambda x: (x[1],x[0]))

    for guest in groups:
        



    print(accommodated)
        

#print(accommodate(5, 4, 2,room_305=6, room_410=5, room_204=2))
print(accommodate(10, 9, 8,room_307=6, room_802=5))
#print(accommodate(1, 2, 4, 8,room_102=3, room_101=1, room_103=2))