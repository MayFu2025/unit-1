## if statements ##
# Aug 24 2023 #

Check for positive/negative number
```.py
#Validate user input
while True:
    raw_number = input("Enter a number: ")
    if raw_number[0] == '-':
        if raw_number[1:].isnumeric(): #This way of validating will only work when the user inputs a whole negative number. It does not work for positive/negative floats, as the isnumeric() function will return False due to the '-' '+' '.' symbols.
            number = int(raw_number)
            break
    if raw_number.isdigit() == True:
        number = int(raw_number)
        break

#Check if input number is positive or negative
if number >= 0:
    print("The number is positive")
else:
    print("The number is negative")
```

Sort 3 numbers from least to greatest
```.py
#Validate user inputs
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

#Check for order from largest to smallest using if statements
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

Coding Exercise 3: Write a program to sort alphabetically three names entered by the user. Note: Assume that only the first letter of names are the same.
*My program for this does not use if statements...
```.py
#Validate user inputs
while True:
    raw_name_a = input("Enter the first name: ")
    if raw_name_a.isalpha():
        name_a = raw_name_a
        break

while True:
    raw_name_b = input("Enter the second name: ")
    if raw_name_b.isalpha():
        name_b = raw_name_b
        break

while True:
    raw_name_c = input("Enter the third name: ")
    if raw_name_c.isalpha():
        name_c = raw_name_c
        break

#Sort user inputs into alphabetical order
names = [name_a.title(), name_b.title(), name_c.title()] #Creates a list of user inputs. The function title() is used to make sure names are capitalized.
names.sort() #sort() function sorts strings into alphabetical order. Sorts numbers into smallest to biggest if reverse parameter is not specified.
print(names)
```
