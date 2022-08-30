import numpy as np

empty_list = np.empty(10, dtype=int)
empty_list.fill(4)
print(empty_list)

multiple_list = np.array([[2, 3, 4, 5], [5, 7, 8, 9], [6, 5, 4, 3]]) * 2
print(multiple_list)

range_list = np.arange(0, 1001)
print(range_list)

power_list = np.arange(0, 11)
a = np.power(power_list, 3)
print(a)

first_array = np.array([[1, 2, 3], [4, 5, 6]])
second_array = np.array([[5, 6, 3], [4, 7, 2]])
final_array = np.add(first_array,second_array)
print(final_array)
copy = np.copy(final_array)
print(copy)

