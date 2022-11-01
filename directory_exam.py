import os
import shutil
from os import path
from zipfile import ZipFile

input_path = r"C:\Users\a.zare\Desktop\file system exam"
out_path = r"C:\Users\a.zare\Desktop\out\data"  # get relative path by ./out to get zip file
out_pathhh = r"C:\Users\a.zare\Desktop\out"
zip_file = r"C:\Users\a.zare\Desktop\out\text.zip"
move_path = r"C:\Users\a.zare\Desktop\out\data"
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


# with open("C:\Users\arezoo\Desktop\out")


for item in get_path(input_path):
    file_size = path.getsize(item)
    read_file = open(item, "r")
    read_line = read_file.readline()
    read_file.close()
    word_name = ""
    has_error = False

    if file_size >= 100:
        with open(os.path.join(out_path, "error_file.txt"), "a") as file:
            file.write(item + " too big to process" + "\n")

        has_error = True

    elif file_size == 0:
        with open(os.path.join(out_path, "error_file.txt"), "a") as f:
            f.write(item + " empty file can't be process" + "\n")
        os.remove(item)
        has_error \
            = True

    # if not has_error and read_line != "\n":
    #     if len(read_line) <= 10:
    #         word_name += read_line
    #     else:
    #         if read_line[9] == " ":
    #             word_name += read_line[0:9]
    #         elif read_line[10] == " ":
    #             word_name += read_line[0:10]
    #         else:
    #             if " " in read_line[0:10]:
    #                 a = read_line[0:10].rfind(" ")
    #                 word_name += read_line[0:a]
    #             else:
    #                 word_name += read_line[0:10]
    # elif not has_error and read_line == "\n":

    # \\ is read by os
    # / prefer to determine path
    # dest_item = "\\".join(item.split("\\")[:-1]) + "\\" + word_name + ".txt"
    # dest_item = move_path + "/" + word_name + ".txt"
    # os.rename(item, dest_item)
    if not has_error and read_line == "\n":
        # last_part = item.split("\\")[-1]
        # name = last_part.split(".")[-2]

        with open(os.path.join(out_path, "error_file.txt"), "a") as unti:
            unti.write("\\".join(item.split("\\")[:-1]) + "\\" + "untitled.txt" + "\n")

with open(os.path.join(out_path, "error_file.txt"), "r") as unti_files:
    unti_file = unti_files.readlines()
    sum_untitle = "untitled.txt"
    i = 0
    for fg in unti_file:
        if "untitled.txt" in fg.split("\\")[-1]:
            if i > 0:
                sum_untitle = "untitled_" + "copy" + str(i)
            i += 1
            # os.rename()
            print(sum_untitle)
# for item in get_path(input_path):
#     with open(path.join(out_path, "all_files.txt"), 'a') as f:
#         f.write(item + "\n")
#
# with ZipFile(zip_file, "w") as zip:
#     zip.write(path.join(out_path, "all_files.txt"))
#
