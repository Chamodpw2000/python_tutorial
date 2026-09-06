age = 22
if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")

print("Eligible" if age >= 18 else "Not Eligible")


for _ in range(5):
    print("Hi Digital T3")
numbers = [1,1,1,1,1,7,8]
for number in numbers:
    if(number%2==0):
        print("Found an even number")
        break
else:
    print("All numbers are odd")
    
