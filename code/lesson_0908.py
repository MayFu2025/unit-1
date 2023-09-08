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




# September 8th lesson: importing data

with open("../database_lesson_0908.csv", 'r') as myfile:
    database = myfile.readlines()
print(database)

items = []
prices = []

for line in database:
    line = line.strip() #removes \n
    name, price = line.split(',') #stores each side as each variable when split by comma
    items.append(name)
    prices.append(int(price))

# items = ['onigiri', 'bread', 'chips', 'coffee', 'ice cream']
# prices = [500, 200, 150, 100, 150]




title = 'Welcome to Combini!'
total = 0
logo = """
         _.-.
       ,'/ //\.
      /// // /)
     /// // //|
    /// // ///
   /// // ///
  (`: // ///
   `;`: ///
   / /:`:/
  / /  `'
 / /
(_/  Combini
"""

print(logo)
print(f"{frame_maker(msg=title, symbol='*', spaces=19)}\n") #Make frame

print("Menu".center(50,' ')) #Print Menu
for it in range(len(items)):
    print(f"{it+1}. {items[it].title().ljust(50, '.')}{prices[it]}yen")

order = [] #Empty list for user order
ordering = True

while ordering:
    selection = (input(f"\nPlease enter a item number (1-{len(items)}): "))
    available = "" #Empty string
    for i in range(len(items)): #For loop to append the numbers user can input
        available += str(i+1)
    while not (selection.isdigit() and selection in available): #Don't trust the user.
        selection = (input(f"Error. Please enter a item number (1-{len(items)}): "))

    order.append(int(selection)-1) #Append order to cart
    total += prices[int(selection)-1]

    for it in range(len(items)):
        count = 0
        for o in order:
            if o == it:
                count += 1
        if count > 0:
            total_price = prices[it]*count
            print(f'{items[it].title().ljust(20)} x {count} = {total_price}yen')

    answer = input("\nWould you like to check out? (Y/N:)  ")
    while not answer in "yYnN":
        answer = input("\nError. Check out? (Y/N):  ")

    if answer in "yY":
        ordering = False


print(frame_maker(msg=f"Your total is {(total*1.1):.2f} yen.", symbol='*', spaces=19))


# CREATE NEW CSV FILE WHICH SAVES THE TOTAL FROM EACH TIME THE CODE IS RUN
with open("sales_lesson_0908.csv", 'a') as myfile:
    myfile.writelines(f"order date total {total*1.1:.2f}\n")