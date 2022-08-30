import pandas as pd

# base_path = r"C:\personal_files"
# input_data = os.path.join(base_path, "employee_dataset.txt")
# read_data = pandas.read_csv(input_data, delimiter="\t")

#
# --------------
# print(df[["Employee_Job_Title","Company_Name"]].values)
# print(pd.unique(df[["Company_Name","Employee_Salary"]].values.ravel()))
# print(set(df["Company_
# # def get_column(employee_attribute):
# #     employee_result = df[employee_attribute]
# #     return employee_result
# #
# #
# # df = pandas.DataFrame(read_data)
# # print (get_column("Employee_Salary").mean())
# # print (get_column("Employee_Salary").max())
# # print (get_column("Employee_Salary").min())
# # print("colmun_num:" , len(df.columns))
# # print("colmun_name:", df.columns)
# # print (df["Company_Name"].unique())
# # print(df.loc[:,["Name"]])
# # print(df.loc[df['Name']=='Julie Morton'])
# # print(df.keys())Name"]))
# print(pd.concat([df["Company_Name"],df["Employee_Salary"]]))
# print (len(df["Company_Name"].unique()))

indexes = ["Name", "Company_Name", "Employee_Job_Title", "Employee_City", "Employee_Country", "Employee_Salary",
           "Employment_Status", "	Employee_Rating"
           ]
# read_data.columns = indexes
# print(get_column('Company_Name'))
# mask = read_data["Employee_Salary"] > 900000
# a=read_data[mask]
# print(a)
# mask = read_data.Employee_Country == "Japan"
# a = read_data[mask]

# --------------
# df = pd.DataFrame({
#     "A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"]
#     , "B": ["one", "one", "two", "three", "two", "two", "one", 'three']
#     , "C": np.random.randn(8), "D": np.random.randn(8)})
# for key in df.keys():
#     print(df[key].value_counts())
# ----------------
# today = pd.to_datetime("today")
# date_range = pd.date_range(today, periods=6, freq="H")
# print(date_range)
# ----------------

# print(read_data.iloc[-3:])
# a = read_data.groupby(by=["Company_Name"]).value_counts()
# print(a)
# print(read_data.iloc[:5])

first_df = pd.DataFrame([["shiraz", 1500000], ["esfehan", 2700000], ["tabriz", 1450000]], columns=["city", "pop"])
first_df["area"] = [500, 340, 780]
second_df = pd.DataFrame([["ahvaz", 670000], ["rasht", 560000]], columns=["city", "pop"])
# merged_df = pd.merge(first_df, second_df, on=["city", "pop_x"])

frames = [first_df, second_df]



print(pd.concat(frames))
