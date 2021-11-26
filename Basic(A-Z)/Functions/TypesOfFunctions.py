# Two Types of functions

# 1 Perform a task
def person(name):
    print(f"My name is {name}")


# 2 Calculate and return value
# round(1.9)

def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("Omar")
print(message)

# By default python return all value None

def greetings(name):
    print(f"hey hi {name}")


print(greetings("Omar"))