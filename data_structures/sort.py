items = [
    ("Product1", 10),
    ("Product2",12),
    ("Product3",23)
]


def sorted(item):
    return item[1]
items.sort(key=sorted)
print(items)

# A lambda function is a small anonymous function. A lambda function can take any number of arguments, but can only have one expression.

items.sort(key=lambda item: item[1])

print(items)