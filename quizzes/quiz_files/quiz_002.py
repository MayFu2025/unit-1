#TODO: SL needs its own function...?

#HL
def check_20(list1:list, list2:list)->bool:
    for item in list1:
        if item == 20:
            return True
    for item in list2:
        if item == 20:
            return True
    for n in range(len(list1)):
        if list1[n] + list2[n] == 20:
            return True
    return False

check1 = [10, 30, 10, 26]
check2 = [20, 15, 5, -6]
print(check_20(list1= check1, list2= check2))