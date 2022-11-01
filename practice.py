import time

import bs4
import requests
from bs4 import BeautifulSoup

categories = [
    "camera",
    "roadblock",
    "roadoperation",
    "roadaccident",
    "weather",
    # "passenger",
    "emdad",
    "repair",
    "gasstation",
    "complex",
    "mosque",
    "hospital",
    "tollhouse",
    "otfapi",
    "vms",
    # "accident-points"
]

for item in categories:
    time.sleep(2)
    try:
        res = requests.post(f"https://141.ir/api/{item}", {"device_type":4})
        print(res.json(), item, "\n\n\n_____________________________________\n" )
    except:
        print("error",item)


# tt = requests.get("https://141.ir")
# bs = bs4.BeautifulSoup(tt.content)
# a = bs.find(attrs={"id": "RespVerticalMenuId"})
# buttons = a.find_all("button")
# print(buttons)
# # url='http://quotes.toscrape.com/'
# # response=requests.get(url)
# print(response.status_code)

# """
# <div id="box" data-item="2"></div>
# """
# a = {
#     "name": "div",
#     "attrs": {
#         "id": "box",
#         "data-item": "2"
#     }
# }
