num=int(input("Enter a number: "))
x=0
if num>0:
    for i in range(1,num+1):
        x+=1
        for j in range(i):
            print(x,end=" ")
            
        print()