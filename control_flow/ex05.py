num=input("Enter a number: ")
if len(num)==4 and num.isdigit():
    digits=[]
    for x in num:
        digits.append((int(x)+3)%10)
    digits[0],digits[2]=digits[2],digits[0]
    digits[1],digits[3]=digits[3],digits[1]

print(digits,sep="")