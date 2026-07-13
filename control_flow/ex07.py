total=0
product=int(input("Enter the product number:"))

while product!=0:
    if 1<=product<=5:
    
        quantity=int(input("Enter the quantity:"))
    
        match product:
            case 1:
                total+=quantity*2.98
            case 2:
                total+=quantity*4.50
            case 3:
                total+=quantity*9.98
            case 4:
                total+=quantity*4.49
            case 5:
                total+=quantity*6.87
            case _:
                print("Invalid number!")
    
       
    else:
        print("Invalid number")
    product=int(input("Enter the product number:"))
total=round(total,2)



print(f"Total is {total}")