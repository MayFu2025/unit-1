# Quiz 003
## Aug 8 2023
<img width="902" alt="Screenshot 2023-09-08 at 12 45 58" src="https://github.com/MayFu2025/unit1_repo/assets/122759229/f6954fb2-860b-4921-8633-f01bbb257e59">

Flow Diagram:
![](/quizzes/assets/Quiz003.jpg)
*fig. 1* Flow diagram of solution

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
![Screenshot 2023-09-03 at 16.34.37.png](..%2F..%2F..%2F..%2F..%2Fvar%2Ffolders%2Fqh%2Fl7367_q936d7t2_57vd5fkjw0000gn%2FT%2FTemporaryItems%2FNSIRD_screencaptureui_m0hl5M%2FScreenshot%202023-09-03%20at%2016.34.37.png)
