# Quiz 008
## Sep 8, 2023

Screenshot of quiz

Flow Diagram of Solution:

*fig. 1* Flow diagram of solution to quiz 008

Solution:
```.py
def cipher_message(msg:str, shift:int)->str:
    msg.lower()
    ciphered = ''

    for let in msg:
        if let.isalpha():
            num = ord(let)
            num += shift

            if num > 122:
                num -= 26
            elif num < 96:
                num += 26

            ciphered += chr(num)
        else:
            ciphered += let

    return ciphered
```

Proof:
