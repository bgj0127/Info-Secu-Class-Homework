import random

i = 0
while i < 100:
    print("while문 반복",i)
    i += 1


i = 0
while i != 3:
    i = random.randint(1, 6)
    print(i)


