# my_lib.py
def frame_maker(msg:str, symbol:str, spaces:int)->str:
    height = 5
    width = 2+2*spaces+len(msg)
    cyan = "\33[0;36m"
    end_code = "\33[0m"

    top_line = symbol*width
    middle_line = symbol + (" "*(width-2)) + symbol
    msg_line = symbol + " "*spaces + msg.title() + " "*spaces + symbol
    banner = f"{top_line}\n{middle_line}\n{msg_line}{end_code}\n{middle_line}\n{top_line}"

    return banner

def print_menu(menu):
    for it in range(len(menu)):
        print(f"{it + 1}. {menu[it].title()}")


def validate_int(msg : str, menu):
    option = input(msg)
    while not option.isdigit():
        print("[ERROR]")
        print_menu(menu)
        option = input("Please enter an option: ")
    return int(option)
