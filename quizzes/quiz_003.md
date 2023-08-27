# Quiz 003 #
## Aug 8 2023 #

(insert quiz slide)

My Solution:
```.py
def convert_protein(in_protein:str)->str:
    out_protein = ''
    for letter in in_protein:
        if letter == 'A':
            out_protein += 'T'
        elif letter == 'G':
            out_protein += 'C'
        elif letter == 'T':
            out_protein += 'A'
        elif letter == 'C':
            out_protein += 'G'
    return out_protein
```

Checking that it works:
```.py
print (convert_protein('A'))
print (convert_protein('G'))
print (convert_protein('C'))
print (convert_protein('T'))
print (convert_protein('AGCT'))
```
Output in the console:
<img width="924" alt="Screenshot 2023-08-28 at 8 31 24" src="https://github.com/MayFu2025/unit-1/assets/122759229/ee6e5c0e-a7f8-428c-9a24-58f2f288c15f">
