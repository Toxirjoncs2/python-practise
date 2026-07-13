num=int(input("How many numbers you want to input: "))
numbers=[]
for i in range(1,num+1):
    numbers.append(int(input(f"Enter number{i}: ")))
new=[x**3 for x in numbers if x%2!=0]
print(new)