
positive=0
negative=0
num=int(input("Enter a number: "))
total=num
if num>=1:
    positive=1
elif num<0:
    negative=1
while num!=0:
    num=int(input("Enter a number: "))
    total+=num
    if num>=1:
        positive+=1
    elif num<0:
        negative+=1
    average=float(total/(positive+negative))

print(f"The number of positives is {positive}")
print(f"The number of negative is {negative}")  
print(f"The total is {total}") 
print(f"The average is {average}")



