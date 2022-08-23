import re

regex = "\d+\.\d+"
a = "45.6"
ad = re.match(regex,a)
print(ad)
