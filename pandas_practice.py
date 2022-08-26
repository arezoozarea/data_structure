import os
import re

import pandas

base_path = r"C:\personal_files"
input_data = os.path.join(base_path, "employee_dataset.txt")
read_data = pandas.read_csv(input_data, delimiter="\t")
df = pandas.DataFrame(read_data)
employee_salary = df["Employee_Salary"]
print (employee_salary.mean())
print (employee_salary.max())
print (employee_salary.min())
print("colmun_num:" , len(df.columns))
print("colmun_name:", df.columns)
print (df["Company_Name"].unique())
print(len(df.loc[df['Company_Name']=='Nichols-James']))
# --------------
# print(df[["Employee_Job_Title","Company_Name"]].values)
# print(pd.unique(df[["Company_Name","Employee_Salary"]].values.ravel()))
# print(set(df["Company_Name"]))
# print(pd.concat([df["Company_Name"],df["Employee_Salary"]]))
# print (len(df["Company_Name"].unique()))

def get_column(employee_attribute):
    employee_result = df[employee_attribute]
    return employee_result

print(get_column('Company_Name'))

