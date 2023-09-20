# ATM
# Deposit, Check balance, Withdraw
import datetime

from lesson_0920_my_lib import frame_maker, print_menu, validate_int

msg = frame_maker("Welcome to ATM", '$', 50)
print(msg)


menu = ["Deposit", "Withdraw", "Balance", "Graph"]
print("The menu is:")
print_menu(menu)

# option = input("Please enter an option: ")
# while option not in "123":
#     print("Error.")
#     print_menu(menu)
#     option = input("Please enter an option: ")

option = 0
while option not in (1, 2, 3, 4):
    option = validate_int(msg="Please enter an option: ", menu=menu)

if option == 1:  # Deposit
    amount = validate_int(msg="Please enter amount to deposit: ", menu='')
    date = datetime.date.today()  # Gives us today's date
    line = f"{date},{amount}\n"
    with open('lesson_0920_atm.csv', mode='a') as f:
        f.writelines(line)
    print("Complete")

if option == 3: # Calculate balance
    with open('lesson_0920_atm.csv', mode='r') as f:
        data = f.readlines()
    balance = 0
    for line in data:
        date, amount = line.strip().split(',') # if you have more elements you need more variables
        balance += int(amount)
    today = datetime.date.today()
    msg = f"Your balance {today} is ${balance}"
    print(frame_maker(msg, '$', 50))

    # This shows balance as 0 even when there is a deposit from that date?
    # today = datetime.date.today()
    # for line in data:
    #     date, amount = line.strip().split(',')
    #     if date == today:
    #         balance += int(amount)
    # msg = f"Your balance {today} is ${balance}"
    # print(frame_maker(msg, '$', 50))

if option == 4:
    with open('lesson_0920_atm.csv', mode='r') as f:
        data = f.readlines()
    deposits = 0
    withdraws = 0
    for line in data:
        date, amount = line.strip().split(',')
        if int(amount) > 0:
            deposits += int(amount)
        else:
            withdraws += (-1*int(amount))
    print(deposits, withdraws)

    # create a simple graph
    deposits = deposits//100
    withdraws = withdraws//100
    bar_deposits = "deposits".ljust(20)
    for x in range(deposits):
        bar_deposits += '▥'
    bar_withdraws = "withdraws".ljust(20)
    for x in range(withdraws):
        bar_withdraws += '▥'
    print(f"{bar_deposits} ${deposits*100}\n{bar_withdraws} ${withdraws*100}")