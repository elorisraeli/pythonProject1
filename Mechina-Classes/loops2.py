# Exercise: ---Jumps by 0.1---
for x in range(5):
    for y in range(10):
        if y == 0:
            print(int(x))
        else:
            print(round(x + (y * 0.1), 1))

# Exercise: ---Number 6 in cube---
import random

counter = 1
while True:
    num = random.choice([1, 2, 3, 4, 5, 6])
    print(num)
    if num == 6:
        break
    counter += 1
print(f"The amount that took to get number 6 is: {counter} cube drop")
