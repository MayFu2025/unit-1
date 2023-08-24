## Variables, Inputs, and Outputs ##
# August 23, 2023 #

```.py
'''
Input output and functions
August 23 2023
'''

my_name = 'May Fujita' #String: In single or double quotations
my_email = '2025.may.fujita@uwcisak.jp'
is_student = True #Boolean: True/1 or False/0
my_age = 16 #Integer: whole numbers
my_height = 161.4 #Float: decmial numbers

#Show messages with print function
print(my_name)
print(my_email, my_age, end="") #Claiming to want nothing at the end: shows in same line
print(my_height)

#f-string allows for combinations of string and python code
print(f"Welcome {my_name}, your email is {my_email}.")

#inputs can be saved in variables, will take user input as string
position = input("Please enter your position")
salary = int(input("Please enter your salary in JPY"))
print(f"Your position is {position}, and salary is {salary}.")

```

```.py
Validating correct inputs from user. Needs to be done every time there is an input from the user. Do not trust the user.
 while True:
     raw_year = input("What year will you graduate ISAK? ")
     if raw_year.isdigit() == True:
         year = int(raw_year)
         break

 while True:
     raw_first_name = input("What is your first name? ")
     if raw_first_name.isalpha() == True:
         first_name = raw_first_name.lower()
         break

 while True:
     raw_last_name = input("What is your last name? ")
     if raw_last_name.isalpha() == True:
         last_name = raw_last_name.lower()
         break

email1 = f"{year}.{first_name}.{last_name}@uwcisak.jp"

print(f"Your school email is: {email1}")



while True:
    raw_email = input("What is your emailaddresss? ")
    if '@' in raw_email:
        email2 = raw_email.lower()
        break

if email2.endswith('@uwcisak.jp'):
    print("Welcome to ISAK!")
else:
    print("You are not allowed!")
```
