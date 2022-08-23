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


# -----------------------------------------------------
from datetime import date


def validate_year():
    years_list = []
    while True:
        input_year = input("enter year:")

        if input_year == "end":
            break
        else:
            cur_year = date.today().year
            if 2000 <= int(input_year) <= cur_year:
                years_list.append(input_year)
            else:
                print("invalid_year")
    print(years_list)


validate_year()
