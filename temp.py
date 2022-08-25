import re

a = "arezoo is ahard worker"
b = "zo"
split_a = a.split(" ")
if b in split_a[0]:
    print(b)