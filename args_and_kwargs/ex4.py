def employee_info(*args, **kwargs):
    print("\nSkills:")
    for skill in args:
        print("-",skill)
    print("\nPersonal informations:")
    for key,value in kwargs.items():
        print(f"{key}: {value}")
employee_info(
    "Python",
    "Postgresql",
    "Django",
    "Git/Github",
    name=input("Enter your name: "),
    age=int(input("Enter your age: ")),
    city=input("Enter your location: ")
)