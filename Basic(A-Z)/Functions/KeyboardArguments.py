def increment(number, by=1):
    return number + by


print(increment(2, 3))


def save_user(**user):
    print(user)


save_user(id=1, name="jhon", age=22)
