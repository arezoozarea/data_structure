import requests
from bs4 import BeautifulSoup

# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# url = raw_input('enter url: ')
# html = urllib.urlopen(url, context=ctx).read()
url = "https://google.com"
html = requests.get(url).text

soup = BeautifulSoup(html, "html.parser")

divs = soup("div")

print divs[0].getText()
