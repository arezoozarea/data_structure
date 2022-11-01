import re

regex = ".*تلفن"
string = "<li>جایگاه شهریار ۱۱۰: جاده  تهران شهریار. نرسیده به میدان نماز سمت چپ. تلفن: ۶۵۲۶۸۸۹۳</li>"
a = re.findall(regex,string)
print(a)