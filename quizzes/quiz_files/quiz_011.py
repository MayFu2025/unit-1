while True:
    number = int(input('Enter a number between 2 and 10: '))
    if 2 < number < 10:
        break
    else:
        number = int(input('Error. Please enter a number between 2 and 10: '))


def multiplication_table(n: int) -> str:
    output = ''
    for i in range(1,10):
        output += f'{n} x {i} = {n*i}\n'
    return output


print(multiplication_table(n=number))

