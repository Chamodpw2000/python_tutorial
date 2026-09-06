from sys import getsizeof
values = (x*2 for x in range(1000000000000000) )
print("gen:", getsizeof(values))
values = [x*2 for x in range(1000000000000000) ]
print("list:", getsizeof(values))
# gen has no len it will give error. 

 
