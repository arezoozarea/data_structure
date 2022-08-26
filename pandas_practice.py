import os

import pandas

base_path = r"C:\personal_files"
input_data = os.path.join(base_path, "employee_dataset.txt")
read_data = pandas.read_csv(input_data, delimiter="\t")


def get_column(employee_attribute):
    employee_result = df[employee_attribute]
    return employee_result


df = pandas.DataFrame(read_data)
print (get_column("Employee_Salary").mean())
print (get_column("Employee_Salary").max())
print (get_column("Employee_Salary").min())
print("colmun_num:" , len(df.columns))
print("colmun_name:", df.columns)
print (df["Company_Name"].unique())
print(df.loc[:,["Name"]])
print(df.loc[df['Name']=='Julie Morton'])
# --------------
# print(df[["Employee_Job_Title","Company_Name"]].values)
# print(pd.unique(df[["Company_Name","Employee_Salary"]].values.ravel()))
# print(set(df["Company_Name"]))
# print(pd.concat([df["Company_Name"],df["Employee_Salary"]]))
# print (len(df["Company_Name"].unique()))


# print(get_column('Company_Name'))
