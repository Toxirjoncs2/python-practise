num=int(input("Enter the number of classes: "))
total_credit=0
total=0
while num>0:
    credits=int(input(f"Enter the credit for course {num}: "))
    grade=float(input(f"Enter the grade for course {num}: "))
    num-=1
    total+=credits*grade
    total_credit+=credits

avg=total/total_credit
print(f"Average grade is {avg}")