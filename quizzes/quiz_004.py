print("hello world")
def check_factors(number: int):
    list = []
    for i in range(1,number+1):
        if number % i == 0:
            list.append(i)
    if list == [1, number]:
        list.append('True')
    else:
        list.append('False')
    return list


print(check_factors(28))