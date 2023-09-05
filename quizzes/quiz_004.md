# Quiz 004 #
## Sep ? 2023 #



Flow Diagram:

*fig. 1* Flow diagram of solution

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

Checking that it works:
![Screenshot 2023-09-05 at 11.14.01.png](..%2F..%2F..%2F..%2F..%2Fvar%2Ffolders%2Fqh%2Fl7367_q936d7t2_57vd5fkjw0000gn%2FT%2FTemporaryItems%2FNSIRD_screencaptureui_z1FfwJ%2FScreenshot%202023-09-05%20at%2011.14.01.png)