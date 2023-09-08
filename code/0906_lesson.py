#Using For Loops
multiples = 0
for n in range(1,100+1):
    if n%7 == 0 and n%6 == 0:
        print(f'{n} is a multiple of 6 and 7.')
        multiples += 1
print(f'There are {multiples} number of multiples of 6 and 7 between 1 and 100.')


#Using While Loops
count = 0
num = 1
while count < 500:
    if num % 7 == 0 and num % 6 == 0:
        print(f'{num} is a multiple of 6 and 7.')
        count += 1
    num += 1
print(f'We counted to {num} to find 500 multiples.')