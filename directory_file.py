import os
from os import listdir
import shutil, os

def get_file(path):
    text_list = []
    cur_path = listdir(path)
    dirName =r"C:\Users\arezoo\Desktop\data\data2\data\file_paths"
    for item in cur_path:
        full_path = os.path.join(path, item)
        if not full_path.endswith("txt"):
            text_list.append(get_file(full_path))
        else:
            text_list.append(full_path)
    if not os.path.exists(dirName):
        os.makedirs(dirName)


print(get_file(r"C:\Users\arezoo\Desktop\data"))
