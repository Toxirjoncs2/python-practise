num=int(input("Enter a number: "))
count=0
result=2**(count+1)

while num>result:
    count+=1
    result=2**(count+1)
print(count)