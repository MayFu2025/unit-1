input = input('Enter a string:  ')
strings = input.split()

output = ''
for word in strings:
    if len(word) <= 2:
        output += word+' '
    else:
        output += word[0]+str(len(word)-2)+word[-1]+' '

print(output)