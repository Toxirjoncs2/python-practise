num=int(input("How many words you want to enter: "))
words=[]
for i in range(1,num+1):
    words.append(input(f"Enter word{i}: "))
five_or_more_words=[x for x in words if len(x)>=5]
print(five_or_more_words)