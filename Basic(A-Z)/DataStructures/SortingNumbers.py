# numbers = [3, 15, 14, 8, 9]
# numbers.sort()
# numbers.sort(reverse=True)
# print(numbers)

items = [
    ("Product1", 10),
    ("Product2", 6),
    ("Product3", 5)
]


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)
