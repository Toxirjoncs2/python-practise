print("Enter 10 numbers")
count=0
digits=[]
while count!=10:
    digits.append(input(f"Enter the number {count+1}: "))
    count+=1
for i in range(0,9): 
    for x in range(i+1,10):
        print(digits[i]+" "+digits[x])
