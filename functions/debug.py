def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total

print("Start")
print(multiply(1,2,3,4))

'''

F9 = Set debug point
F5 = Start debug
F10 = Step over
F11 = Step into
Step over means executing the current line and moving to the next line without entering any function calls.
Step into means entering the function call on the current line.
Shift + F5 = Stop debug
Shift + F11 = Step out
Step out means executing the remaining lines of the current function and returning to the caller function.

'''