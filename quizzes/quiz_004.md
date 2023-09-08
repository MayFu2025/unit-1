# Quiz 004 #
## Sep ? 2023 #



Flow Diagram:
![](/quizzes/assets/Quiz004.jpg)
*fig. 1* Flow diagram of solution to quiz 004

My Solution:
```.py
def check_factors(number: int):
    list = []
    for i in range(1,number+1):
        if number % i == 0:
            list.append(i)
    if list == [1, number]:
        list.append('True')
    else:
        list.append('False')
    return list
```

Proof:
<img width="1157" alt="Screenshot 2023-09-08 at 12 44 44" src="https://github.com/MayFu2025/unit1_repo/assets/122759229/bdff38ec-c24c-4dc3-aa25-16b8b4fece89">
