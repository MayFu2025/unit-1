# #SL
# def sum_letters(text:str) -> int:
#     alphabet = 'abcdefghijklmnopqrstuvwxyz'
#     sum_total = 0
#
#     for let in text:
#         index = -1
#         for i in range(len(alphabet)):
#             if let == alphabet[i]:
#                 index = i+1
#                 sum_total += index
#     return sum_total

#HL Math -> 1385
def sum_letters(text:str) -> int:
    sum_total = 0
    for let in text:
        sum_total += ord(let)
    return sum_total


print(sum_letters(text='hello'))
