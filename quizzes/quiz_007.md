# Quiz 007
## Sep 7, 2023


Flow diagram of solution:
![](/quizzes/assets/Quiz007Diagram.jpg)
*fig. 1* Flow diagram of solution to Quiz 007

Solution:
```.py
import random

count = 0
n = random.randint(1, 100)

while n>15:
    count += 1
    n = random.randint(1, 100)
print(f"It took {count} tries to generate a number less than or equal to 15.")
```

Proof:
<img width="1157" alt="Screenshot 2023-09-08 at 12 41 13" src="https://github.com/MayFu2025/unit1_repo/assets/122759229/4b659221-1c82-444d-9d8c-afc9f3c3554d">

