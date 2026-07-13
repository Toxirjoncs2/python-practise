import time
n=int(input("Enter a number: "))
while n>1:
    time.sleep(1)
    n-=1
    print(f"{n} seconds remaining")
print("Stopped")