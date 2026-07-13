import math
flag=False
number=int(input("Enter a number: "))
if number==0 or number==1:
    print("It is not a prime number")
elif number>1:
    for i in range(2,int(math.sqrt(number))+1):
        if number%i==0:
            flag=True
            break
    if flag==True:
        print("Not prime")
    else:
        print("Prime")
else:
    print("It is a negative number")     
        
    
        