point = {"x": 1, "y": 2}

point2 = dict(x=1, y=2)

print(point["x"])
point["z"] = 4
del point["x"]
if "a" in point:
    print(point["a"])
print(point.get("a",0))


for key in point:
    print(key)
    print(point[key])
    
print(point.items())

for key, value in point.items():
    print(key, value)
    
    