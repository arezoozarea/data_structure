import os
from os import path

input_path = r"C:\Users\arezoo\Desktop\file system exam"
out_path = r"C:\Users\arezoo\Desktop\out"
zip_file = r"C:\Users\arezoo\Desktop\out\text.zip"
move_path = r"C:\Users\arezoo\Desktop\out\data"
if not path.exists(out_path):
    os.makedirs(out_path)
if not path.exists(move_path):
    os.makedirs(move_path)


def get_path(input_path):
    file_list = []
    dirs = os.listdir(input_path)

    for dir in dirs:
        full_path = path.join(input_path, dir)
        if not "New Text Document" in full_path:
            file_list += get_path(full_path)
        else:
            file_list.append(full_path)
    return file_list


for item in get_path(input_path):

    file_size = path.getsize(item)
    if file_size < 100 or file_size != 0:
        read_file = open(item, "r")
        a = read_file.readlines()
        for i in a:
            if i=="\n":
                i.replace("\n","")
            print (i)


# for item in get_path(input_path):
#     with open(path.join(out_path, "all_files.txt"), 'a') as f:
#         f.write(item + "\n")
#
# with ZipFile(zip_file, "w") as zip:
#     zip.write(path.join(out_path, "all_files.txt"))
#
