items = [
    ("Product1", 7),
    ("Product2",12),
    ("Product3",23)
]

def get_price(item):
    return item[1]

x = map(lambda item: item[1],items)
y = map(get_price, items)
z = filter(lambda item : item[1] >= 10, items )
print(list(z))
# print(x)
# map() returns an iterator, not a list. An iterator can only be walked through once — it doesn't store the results, it produces them on demand and keeps a position marker that moves forward.
# for item in x:
#     print(item)
    
# for item in y:
#     print(item)

