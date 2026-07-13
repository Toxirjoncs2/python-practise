def add(*args):
    total=0
    for arg in args:
        total+=arg
    return total
n=int(input("How many numbers you want to input? "))
numbers=[]
for i in range(n):
    number=int(input(f"Enter the number {i+1}: "))
    numbers.append(number)
print(add(*numbers))