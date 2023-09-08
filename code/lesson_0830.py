# Lists
# A variable is like a house with a single room where we store an item. A list is like a hotel with infinite rooms, where the first room number 0.
my_name = "May"  # Variables hold a single value
r4_up_c = ["Elisha", "Mona", "Maryam", "May"]  # Lists hold several values
my_info = [20, "bob", 'bob.square@pants.com', "deepsea"]  # Lists can hold different types of data
print(
    f"Hi my name is {my_info[1]}, I am {my_info[0]} years old.")  # Indexes refer to the position of an item in a lsit, with the first item being 0 in the list being index 0.

# For loops
# For Loops allow us to repeat steps in a program
# index = 0
for item in my_info:
    print(
        f"item {my_info.index(item)}: {item}")  # Alternatively instead of the index() function, you can make a variable that counts up with each loop.
    # index += 1

# Counting the number of characters in the email adress using for loops:
character_count = 0
for letter in my_info[2]:
    character_count += 1
print(f"The number of letters in the email is {character_count}.")

# Doing the same thing using the len() function:
character_count2 = len(my_info[2])
print(f"The number of letters in the email is {character_count2}.")

# Count how many vowels are in the email:
vowel_count = 0
for letter in my_info[2]:
    if letter in 'aeiou':
        vowel_count += 1
print(f"The number of vowels in the email is {vowel_count}. This is {(vowel_count/character_count)*100}% of the email.")

# Print all the numbers from 1 to 2023:
for year in range(1, 2024): # range(start, end(exclusive), step)
    print(f"year {year}")

# Print all the odd numbers from 1 to 1000:
for i in range(1, 1000, 2):
    print(i)

# Print a loop of '012' for 100 characters
for i in range(100): # When repeating you just need to write the number of repeats
    print(i%3, end='')

print() # By default an empty print creates a new line

# Repeat a sequence of items from a list
for i in range(100):
    memes = ['lol', 'omg', 'atp']
    print(memes[i%3], end='-')

