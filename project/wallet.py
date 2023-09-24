import csv, os, datetime
from mylib import startup, function_menu, menu, t_action_menu, display_menu, validate_selection, try_login, login_function, create_user, main_functions

logged_in = False

selection = menu(startup)
if selection == 1:
    output = login_function()
    logged_in = output[0]
    uname = output[1]
if selection == 2:
    create_user()
    output = login_function()
    logged_in = output[0]
    uname = output[1]

if logged_in:
    selection = menu(function_menu)
    main_functions(choice_selected= selection, name= uname)
