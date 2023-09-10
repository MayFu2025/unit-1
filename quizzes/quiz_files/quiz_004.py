def check_factors(number: int) -> list:
    factors = []
    for i in range(1,number+1):
        if number % i == 0:
            factors.append(i)
    if factors == [1, number]:
        factors.append('True')
    else:
        factors.append('False')
    return factors


# Check if function works:
print(check_factors(90))
print(check_factors(31))

