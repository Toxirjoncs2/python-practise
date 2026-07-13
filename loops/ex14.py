total=0
num=int(input("Enter a number: "))
for i in range(1,num+1):
    if i<num:
       print(f"1/{i} +",end=" ")
       
    
    else:
        print(f"1/{i}")
    total+=1/i
print(f"Total is {total}")
