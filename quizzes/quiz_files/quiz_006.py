#SL
count = 0
for f in range(1, 10+1): #for 10 floors
    for r in range(1, 10+1): #for 10 rooms per floor
        count += 1
        print(f'{count}- Room{f}F{r:02d}')


#HL
def locate_room(room_number:int)->str:
    floor = room_number//10
    room = room_number%10
    if room == 0:
        room = 10
    return (f'{room_number}-Room {floor}F{room:02d}')


print(locate_room(78))