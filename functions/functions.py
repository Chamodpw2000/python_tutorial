def greet():
    print("Hi There")


greet()


def greet_user(first_name, last_name):
    print(f"Hi there ! {first_name} {last_name}")


def addition(*numbers):
    total = 0
    for num in numbers:
        total += num
    print(total)


addition(1, 2, 3, 4, 56, 1)


def save_user(**user):
    print(user["name"])


save_user(name="Chamod Path", age=42, id=4)
greet_user("Chamod", "Wanigasekara")


# 2 types of Function are there !
# 1. Perform a task (ALl functions default return None)
# 2. Perform a task and return something.


file = open("content.txt", "w")
file.write("Hi")


def increment(number, by=1):
    return number + by


print(increment(21))
