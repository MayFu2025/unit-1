# Importing Modules
import csv, os, datetime

# Setting Menus, Selections, Functions
startup = ['Already have an account? Log-in', 'New user? Sign-up']
function_menu = ["Create New Transaction", "View Past Transactions", "View Description of DAI Currency", "Log-out"]
t_action_menu = ["Deposit", "Withdraw"]

# Displaying Menu and Validating Menu Selection
def display_menu(choices: list)-> str:
    menu = ''
    count = 1
    for it in choices:
        menu += f"{it.ljust(50, '.')} type {count}\n"
        count += 1
    return menu

def validate_selection(choices: list) -> int:
    expect = len(choices)
    select = input(f'Select a choice between 1~{expect}: ')
    while not 0 < int(select) < expect+1: # TODO: Error when string inputted instead
        select = input(f"Error. Please select a choice between 1~{expect}: ")
    select = int(select)
    return select


# Start-up and Log-in/Create User
def try_login(name: str, password: str) -> bool:
    with open('users.csv', mode='r') as f:
        data = f.readlines()
    success = False
    for line in data:
        uname = line.split(',')[0]
        upass = line.split(',')[1].strip()  # strip() removes \n for any string unless specified
        if uname == name and upass == password:
            success = True
            break
    return success

def login_function() -> tuple:
    in_name = input("Enter your username: ")
    in_pass = input("Enter your password: ")
    success = try_login(in_name, in_pass)
    while success == False:
        print("Wrong username or password. Try again.")
        in_name = input("Enter your username: ")
        in_pass = input("Enter your password: ")
        success = try_login(in_name, in_pass)
    return success, in_name

def create_user():
    with open('users.csv', mode='r') as users_list:
        users_database = users_list.readlines()
    new_name = input("Create a username: ")
    if users_database:
        validate = True
        while validate == True:
            for user in users_database:
                if new_name in user:
                    new_name = input("Username already taken. Please enter another username: ")
                else:
                    validate = False
    new_pass = input("Create a password: ")
    confirm_new_pass = input("Confirm new password: ")
    validate = True
    while validate == True:
        if confirm_new_pass != new_pass:
            new_pass = input("Passwords do not match. Create a password: ")
            confirm_new_pass = input("Confirm new password: ")
        else:
            validate = False
    with open('users.csv', mode='a') as users_list:
        writer = csv.writer(users_list)
        writer.writerow([new_name,new_pass])
    with open(f"{new_name}.csv", 'a') as user_data:
        user_data.writelines(f"{datetime.date.today()},0\n")


# Main Menu and Menu Functions
def main_functions(choice_selected, name):
    action_date = datetime.date.today()
    if choice_selected == 1:
        display_menu(t_action_menu)
        choice = validate_selection(t_action_menu)
        if choice == 1: # User Create Transaction
            raw_dep = input("Enter amount of DAI you would like to deposit: ")
            while not raw_dep.isdigit():
                raw_dep = input("Error. Please enter as a numeric value how much DAI you would like to deposit: ")
            action_value = float(raw_dep)
        if choice == 2:
            raw_wtd = input("Enter amount of DAI you would like to withdraw: ")
            while not raw_wtd.isdigit():
                raw_wtd = input("Error. Please enter as a numeric value how much DAI you would like to withdraw: ")
            action_value = float(raw_wtd)
    with open(f"{name}.csv", 'a') as user_data:
        user_data.writelines(f"{action_date},{action_value}\n")

    if choice_selected == 2: # User View Statistics
        pass

    if choice_selected == 3: # User View DAI Description
        print()

