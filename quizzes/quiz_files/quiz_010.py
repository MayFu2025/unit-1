# def bestMonth():
#     weekdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
#     days_in_may = 31
#     index_week = 0
#     output = ''
#     for n in range(1, days_in_may+1):
#         if index_week > 6:
#             index_week = 0
#         output += f'{weekdays[index_week]} {n} '
#         index_week += 1
#
#     return output
#
# print(bestMonth())

def bestmonth(month: int) -> str:
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    month_length = {
        1: [31, 6],
        2: [28, 2],
        3: [31, 2],
        4: [30, 5],
        5: [31, 0],
        6: [30, 3],
        7: [31, 5],
        8: [31, 1],
        9: [30, 4],
        10: [31, 6],
        11: [30, 2],
        12: [31, 4]}
    index_week = month_length[month][1]
    output = f'{("2023 "+months[month-1]).center(20)}\nMo Tu We Th Fr Sa Su\n{(index_week*3)*" "}'
    for n in range(1, month_length[month][0]+1):
        if index_week % 7 == 0:
            index_week = 0
            output += '\n'
        output += f'{n:02d} '
        index_week += 1
    return output

# Check that it works:
print(bestmonth(month=10))


# ######Class Solution########
# def make_calendar_month():
#     calendar = ''
#     days = ['Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun', 'Mon']
#     for d in range(1, 31):
#         calendar += f'{d:02d} {days[d%7-1]} '
#         if d%7 == 0:
#             calendar += '\n'
#
#     return calendar
#
# print(make_calendar_month())
#
# ##########################
