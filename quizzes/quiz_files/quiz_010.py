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
#
# print(bestMonth())

def bestmonthHL(month: int) -> str:
    weekdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
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
