# SL
#
# count = 0
# for f in range(1, 10+1): #for 10 floors
#     for r in range(1, 10+1): #for 10 rooms per floor
#         count += 1
#         print(f'{count}- Room{f}F{r:02d}')


#HL
def locate_room(room_number:int)->str:
    count = 0
    floor = 0
    for n in range (1, room_number+1):
        for f in range(1, 10+1):
            for r in range(1, 10+1):
                count += 1
            floor += 1
    return (f'{floor}- Room{floor}F{r:02d}')

print(locate_room(1000))
