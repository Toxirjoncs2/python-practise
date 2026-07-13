num=int(input("Enter a number: "))
i=1
pi=0
while i!=num:
    pi+=4*(((-1)**(i+1))/(2*i-1))
    i+=1
print(pi)