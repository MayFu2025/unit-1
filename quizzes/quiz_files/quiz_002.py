#SL
def check_20_sl(num1:int, num2:int)->bool:
    if num1 == 20 or num2 == 20:
        return True
    elif num1 + num2 == 20:
        return True
    else:
        return False

check1 = 30
check2 = 10
print(check_20_sl(num1=check1, num2=check2))

#HL
def check_20_hl(list1:list, list2:list)->bool:
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

check3 = [10, 30, 10, 26]
check4 = [20, 15, 5, -6]
print(check_20_hl(list1= check3, list2= check4))