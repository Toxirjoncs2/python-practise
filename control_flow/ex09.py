import random
rank=random.randint(1,13)
suit=random.randint(1,4)
match rank:
    case 1:
        print("The card you picked is Ace of",end=" ") 
    case 2:
        print("The card you picked is 2 of",end=" ")
    case 3:
        print("The card you picked is 3 of",end=" ")
    case 4:
        print("The card you picked is 4 of",end=" ")
    case 5:
        print("The card you picked is 5 of",end=" ")
    case 6:
        print("The card you picked is 6 of",end=" ")
    case 7:
        print("The card you picked is 7 of",end=" ")
    case 8:
        print("The card you picked is 8 of",end=" ")
    case 9: 
        print("The card you picked is 9 of",end=" ")
    case 10:
        print("The card you picked is 10 of",end=" ")
    case 11:
        print("The card you picked is Jack of",end=" ")
    case 12:
        print("The card you picked is Queen of",end=" ")
    case 13:
        print("The card you picked is King of",end=" ")

match suit:
    case 1:
        print("Clubs")
    case 2:
        print("Diamonds")
    case 3:
        print("Hearts")
    case 4:
        print("Spades")
