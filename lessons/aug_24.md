## if statements ##
# Aug 24 2023 #

```
while True:
    raw_number = input("Enter a number: ")
    if raw_number[0] == '-':
        if raw_number[1:].isnumeric(): #This way of validating will not work for positive/negative floats, as the isnumeric() function will return False due to the '-' '+' '.' symbols.
            number = int(raw_number)
            break
    if raw_number.isdigit() == True:
        number = int(raw_number)
        break

if number >= 0:
    print("The number is positive")
else:
    print("The number is negative")
```

```
#Validate a, b, and c datatypes
while True:
    raw_a = input("Enter first number: ")
    if raw_number.isnumeric() == True:
        a = int(raw_a)
        break

while True:
    raw_b = input("Enter second number: ")
    if raw_number.isnumeric() == True:
        b = int(raw_b)
        break

while True:
    raw_c = input("Enter third number: ")
    if raw_number.isnumeric() == True:
        c = int(raw_c)
        break

#Check using inequalities
if a > b:
    if a > c:
        if b > c:
            print(f"{a}, {b}, {c}")
        else:
            print(f"{a}, {c}, {b}")
    else:
        print(f"{c}, {a}, {b}")
else:
    if b > c:
        if a > c:
            print(f"{b}, {a}, {c}")
        else:
            print(f"{b}, {c}, {a}")
    else:
        print(f"{c}, {b}, {a}")
```
