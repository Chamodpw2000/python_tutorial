values = []
for x in range(5):
    values.append(x*2)
    
values1 = map(lambda x: x*2 , range(5))

values2 = [x*2 for x in range(5)]

# print(values, list(values1) , values2) 

values3 = (x for x in range(5))

print(list(values3))
# print(type(values3))