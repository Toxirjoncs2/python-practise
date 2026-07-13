mile=1
km=1.609*mile

print('|| Miles  |  Kilometers ||')
i=1
for x in range(10):
   
    miles=i*mile
    kms=i*km
    print(f"||{miles:>5}   | {kms:>10.3f}  ||")
    i+=1
    