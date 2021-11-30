items = [
    ("Product1", 10),
    ("Product2", 20),
    ("Product3", 30)
]

prices = list(map(lambda item: item[1], items))
print(prices)