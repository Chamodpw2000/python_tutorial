def fiz_buzz(input):
    if (input % 3 == 0 and input % 5 == 0):
        print("FIZZ BUZZ")
    elif (input % 3 == 0):
        print("FIZZ")
    elif (input % 5 == 0):
        print("BUZZ")
    else:
        print(input)
def fiz_buzz2(input):
    result = ""
    if input % 3 == 0:
        result += "FIZZ"
    if input % 5 == 0:
        result += "BUZZ"
    if (input % 3 != 0 and input % 5 != 0 ):
        return input
    return result 
        
print(fiz_buzz2(15))
print(fiz_buzz2(6))
print(fiz_buzz2(25))
print(fiz_buzz2(17))