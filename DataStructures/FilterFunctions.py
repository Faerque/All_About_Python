items = [
    ("Product1", 10),
    ("Product2", 20),
    ("Product3", 30)
]

filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)