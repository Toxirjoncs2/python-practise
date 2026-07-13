count=0
for x in range(65,91):
    count+=1
    print(chr(x),end=" ")
    if count==5:
        print()
        count=0