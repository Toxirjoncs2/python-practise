import random

odd=0
even=0
for _ in range(100000):
    num=random.randint(1,1000)
    if num%2==0:
        even+=1
    else:
        odd+=1
print(f"Total even numbers:{even}")
print(f"Total odd numbers:{odd}")

