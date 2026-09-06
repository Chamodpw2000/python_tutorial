# [expression for item in items]
items = [
    ("Product1", 7),
    ("Product2",12),
    ("Product3",23)
]

prices = [item[1]+1 for item in items]
filtered = [item for item in items if item[1] >= 10]
print(filtered)