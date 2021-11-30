try:
    with open("TheWithStatement.py") as file:
        print("File Opened")
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You Didn't enter a valid age ")
else:
    print("No exceptions were thrown")
