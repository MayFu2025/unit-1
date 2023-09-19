def bestmonthHL(month: int) -> str:
    weekdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    month_length = {
        1: [31,'Sun'],
        2: [28, 'Wed'],
        3: [31, 'Wed'],
        4: [30, 'Sat'],
        5: [31, 'Mon'],
        6: [30, 'Thu'],
        7: [31, 'Sat'],
        8: [31, 'Tue'],
        9: [30, 'Fri'],
        10: [31, 'Sun'],
        11: [30, 'Wed'],
        12: [31, 'Fri']}
    start_week = month_length[month][1]
    index_week = weekdays.index(start_week)
    output = ''
    for n in range(1, month_length[month][0]+1):
        if index_week % 7 == 0:
            index_week = 0
            output += '\n'
        output += f'{weekdays[index_week]} {n:02d} '
        index_week += 1

    return output


print(bestmonthHL(month=10))

#print(f'{months[month-1]}'.lcenter(20))
#for wd in range(len(weekdays))
#print(f'{}')