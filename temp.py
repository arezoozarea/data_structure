import pandas as pd
#
# data1 = {
#   "name": ["Sally", "Mary", "John"],
#   "age": [50, 40, 30]
# }
#
# data2 = {
#   "name": ["Sally", "Peter", "Micky"],
#   "age": [77, 44, 22]
# }
#
# df1 = pd.DataFrame(data1)
# df2 = pd.DataFrame(data2)
#
# newdf = df1.merge(df2, how='right')
# print(newdf)

a = "best local name"
b = ""
split_text = a.split(" ")
for i in range(len(split_text)):
  if i ==0:
      b += split_text[i]

  else:
      b+=' ' + split_text[i]
  if len(b)<=10:
      name = b
print(name)
# print(b)

