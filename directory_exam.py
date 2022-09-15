import os
from os import path

input_path = r"C:\Users\arezoo\Desktop\file system exam"
dir_name = r"C:\Users\arezoo\Desktop\out"


def get_path(input_path):
    file_list = []
    dirs = os.listdir(input_path)
    if not path.exists(dir_name):
        os.makedirs(dir_name)
    for dir in dirs:
        full_path = path.join(input_path, dir)
        if not "New Text Document" in full_path:
            file_list += get_path(full_path)
        else:
            file_list.append(full_path)
    return file_list


for item in get_path(input_path):
    with open(path.join(dir_name, "all_files.txt"), 'a') as f:
        f.write(item + "\n")

# print(get_path(input_path))
