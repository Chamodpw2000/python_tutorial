import math
x = 1 # Integers
y = 1.1 # Float
z = 1.5 + 2j # Complex

print(round(z.real))
print(math.ceil(z.real))


x = input("Enter a number: ")
print(x)

print(type(x))

y = int(x)

print(type(y))

z = float(x)
print(type(z))

z = bool(x)
print(type(z))

# Falsy values: 0, 0.0, "", None, False

# primitive types -> bool , int , float , complex , str , 
