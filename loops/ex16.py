total=0
power=0
num=int(input("Enter a binary number:"))
while num!=0:
    total+=num%10 * 2**power
    num//=10
    power+=1
print(total)