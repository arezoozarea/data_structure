import re


def validate_name():
    name = input("Enter your name: ")
    if len(name) > 10 or (len(name.split(" ")) > 3):
        print("out of length")
    else:
        print(name)


# ---------------------------------------------------
def validate_age():
    age = input("Enter your age: ")
    float_num = r"\d+\.\d+"
    if re.match(float_num, age):
        print("invalid_type")
    else:
        age = int(age)
        if age < 18:
            print("your age should be at least 18")
        elif age > 40:
            print("your age more than 40")
        else:
            print(age)


validate_age()
