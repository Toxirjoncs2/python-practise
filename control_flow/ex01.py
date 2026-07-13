speed=float(input("Enter the wind speed>=2: "))

temp=float(input("Enter the temperature in Fahrenheit between (-58°F and 41°F): "))
while temp>41 or temp<-58 or speed<2:
    if temp>41 or temp<-58:
        print("Enter the valid number:")
        temp=float(input("Enter the temperature in Fahrenheit between (-58°F and 41°F): "))
    elif speed<2:
        print("Speed should be greater than 2")
        speed=float(input("Enter the wind speed>=2: "))
    else:
        print("Enter the valid number:")
        print("Speed should be greater than 2")
        temp=float(input("Enter the temperature in Fahrenheit between (-58°F and 41°F): "))
        speed=float(input("Enter the wind speed>=2: "))
wind_chill=35.74 + 0.6215*temp-35.75*speed**0.16+0.4275*temp*speed**0.16
print(f"The wind-chill index is {wind_chill,5}")
