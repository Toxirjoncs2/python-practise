def student_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
student_info(full_name=input("Enter your full name: "),
             age=int(input("Enter your age: ")),
             university=input("Enter your university name: "),
             major=input("Enter your major: "))