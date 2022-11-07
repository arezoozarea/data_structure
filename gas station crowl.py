import csv
import re

import pandas
import requests
from bs4 import BeautifulSoup

a = requests.get(
    "https://www.radareghtesad.ir/news/21336/%D9%84%DB%8C%D8%B3%D8%AA-%D8%AC%D8%A7%DB%8C%DA%AF%D8%A7%D9%87-%D9%87%D8%A7%DB%8C-%D9%BE%D9%85%D9%BE-%D8%A8%D9%86%D8%B2%DB%8C%D9%86-%D8%A7%D8%B3%D8%AA%D8%A7%D9%86-%D8%AA%D9%87%D8%B1%D8%A7%D9%86-%D8%A2%D8%AF%D8%B1%D8%B3-%D9%88-%D8%B4%D9%85%D8%A7%D8%B1%D9%87-%D8%AA%D9%84%D9%81%D9%86")

content = BeautifulSoup(a.content, "html.parser")
address = content.find_all("li")[24:241]
for item in address:
    item = re.sub("\s”\s", "", item.get_text()).strip()
    result = re.findall("^(.+). تلفن(| ):",item)
    if result:
        item = result[0][0]
    item = re.sub("[.:]","",item)
    if re.match("^[۰-۹].+",item):
        item = "جایگاه" + item
    item = re.sub("تلفن.*","",item)
    if "جایگاه" not in item:
        item = "جایگاه" + item
    print(item)
