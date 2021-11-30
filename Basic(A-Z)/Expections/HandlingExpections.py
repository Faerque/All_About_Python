try:
    age = int(input("Age: "))
except ValueError:
    print("You didnt enter a valid age")
else:
    print("No executions were thrown")

print("Executions continues")