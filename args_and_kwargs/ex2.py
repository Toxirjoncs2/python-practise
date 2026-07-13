def max_grade(*args):
    max_num=args[0]
    for arg in args:
        if max_num<=arg:
            max_num=arg
        elif not args:
            return None
    return max_num
n=int(input("Enter the number of grades you want: "))
numbers=[]
for i in range(n):
    number=int(input(f"Enter the number {i+1}:"))
    numbers.append(number)
print(max_grade(*numbers))