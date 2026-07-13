import shapes
print("Circle -> 1")
print("Rectangle -> 2")
print("Triangle -> 3")

choice=int(input("Choose a shape: "))
match choice:
    case 1:
        radius=float(input("Enter a radius: "))
        print(f"Area:{shapes.circle_area(radius):.2f}".rstrip("0").rstrip("."))
    case 2:
        a=float(input("Enter length: "))
        b=float(input("Enter width: "))
        print(f"Area:{shapes.rectangle_area(a,b):.2f}".rstrip("0").rstrip("."))
    case 3:
        base=float(input("Enter base: "))
        height=float(input("Enter height: "))
        print(f"Area:{shapes.triangle_area(base,height):.2f}".rstrip("0").rstrip("."))
    case _:
        print("Invalid input")