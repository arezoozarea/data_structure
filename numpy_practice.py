import numpy as np

# empty_list = np.empty(10, dtype=int)
# empty_list.fill(4)
# print(empty_list)
#
# multiple_list = np.array([[2, 3, 4, 5], [5, 7, 8, 9], [6, 5, 4, 3]]) * 2
# print(multiple_list)
#
# range_list = np.arange(0, 1001)
# print(range_list)
#
# power_list = np.arange(0, 11)
# a = np.power(power_list, 3)
# print(a)
#
# first_array = np.array([[1, 2, 3], [4, 5, 6]])
# second_array = np.array([[5, 6, 3], [4, 7, 2]])
# final_array = np.add(first_array,second_array)
# print(final_array)
# copy = np.copy(final_array)
# print(copy)
# ----------------------------
# mulit_array = np.array([[2, 3, 4], [5, 6, 7], [7, 8, 9]])
# print(np.ravel(mulit_array))
# -----------------------------
# array_list = np.array([[2, 3, 4], [1, 2, 3], [5, 2, 4]])
# mask = array_list >=3
# array_list[mask]
# print(array_list[mask])
# -----------------------------
# a = np.array([[2,3,4],[5,6,7]])-2
# print(a)
# -----------------------------
# three_dim_aray = np.array([[3,4,5],[6,7,8],[6,8,9]])
# a = [np.max(arr) for arr in three_dim_aray]
# print(a)
# print(np.max(three_dim_aray))

# array_list = np.array([[2, 3, 4], [1, 2, 3], [5, 2, 4]])
#
# a= np.array([1,2,3,4,11,12])
# mask = a>3
# print(a[a > 10]
#
# three_dim_array = np.array([[3, 4, 5], [1,10,5], [6, 7, 8], [6, 8, 9]])
# print(three_dim_array[2:-1].max())
# print(three_dim_array.max(axis=0))
array1 = np.all([True, False, True, True, False])
array2 = np.array([[34, 5, 6, 5], [4, 78, 5, 4]])
# print(np.all(array2 > 3, axis=1))
# print(np.all(array2))

a = np.array([
    [2, 1],
    [2, 0]
])
result = np.all(a, axis=1)
# print(result)


def valid_all(arr):
    in_data = np.array(arr)
    return np.all(in_data)


print(valid_all([True, False, True, True]))

arr1 = np.arange(16).reshape(4, 4)

arr2 = np.array([1, 3, 2, 5])
arr3=np.array([1, 3, 2, 5])
print(np.sum([arr2,arr1],axis=1))


# np.sum([[0, 1], [np.nan, 5]], where=[False, True], axis=1)