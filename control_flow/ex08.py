year=int(input("Enter year: "))
m=int(input("Enter month (1-12): "))
q=int(input("Enter the day of the month (1-31): "))
if m==1:
    m+=12
    year-=1
    j=year//100
    k=year%100
    
day=(q+(26*(m+1)//10)+k+(k//4)+(j//4)+5*j)%7
match day:
    case 0:
        print("Day of the week is Saturday")
    case 1:
        print("Day of the week is Sunday")
    case 2:
        print("Day of the week is Monday")
    case 3:
        print("Day of the week is Tuesday")
    case 4:
        print("Day of the week is Wednesday")
    case 5:
        print("Day of the week is Thursday")
    case 6:
        print("Day of the week is Friday")
    