num1=int(input("Enter a number 1:"))
num2=int(input("Enter a number 2:"))
num3=int(input("Enter a number 3:"))
if num3%num1==0 and num3%num2!=0:
    print(f"Only {num1} is a factor of {num3}")
elif num3%num1!=0 and num3%num2==0:
    print(f"Only {num2} is a factor of {num3}")
elif  num3%num1==0 and num3%num2==0:
    print(f"Both {num1} and {num2} are the factors of {num3}")
else:
    print(f"{num1} and {num2} are not the factors of {num3}")