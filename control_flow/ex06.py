num=int(input("Enter the number of values to input: "))
count=0

x=int(input(f"Enter the number{count+1} :"))
minimum=x
while count!=num-1:
    
    count+=1
    x=int(input(f"Enter the number{count+1} :"))
    
    if minimum>=x:
        minimum=x
    else:
        minimum=minimum
    
print(minimum)
