#TODO:SL bit is wrong????
def sum_letters_sl(text:str) -> int:
    # alphabet = 'abcdefghijklmnopqrstuvwxyz'
    # sum_total = 0
    #
    # # for let in text:
    # #     for i in range(len(alphabet)):
    # #         index = -1
    # #         if let == alphabet[i]:
    # #             index = i+1
    # #             sum_total += index
    # # return sum_total
    #
    # for let in text.lower():
    #     for i in range(len(alphabet)):
    #         if let == alphabet[i-1]:
    #             sum_total += i+1
    # return sum_total

    sum = 0
    for let in text:
        if let != ' ':
            sum += (ord(let.lower())-96)
    return sum


#HL
def sum_letters_hl(text:str) -> int:
    '''
    as the output for Math in the_hl section on the quiz slides is likely not right,
in my code, I took capital 'A' as 1, and lowercase 'a' as 27.
    '''
    sum_total = 0
    for let in text:
        if let.islower():
            sum_total += ord(let)-64-6
        if let.isupper():
            sum_total += ord(let)-64
    return sum_total


print(sum_letters_sl(text=' '))
print(sum_letters_sl(text='Math'))
print(sum_letters_sl(text='maTH'))
print(sum_letters_sl(text='Hello world'))
print(sum_letters_sl(text='Computer SCIENCE'))

print(sum_letters_hl(text='A'))
print(sum_letters_hl(text='a'))
print(sum_letters_hl(text='Math'))
print(sum_letters_hl(text='maTH'))


