import os
import re
import shutil
from os import listdir, path

# from os import current_path

dir_name = r"C:\Users\a.zare\Desktop\out"

# if path.exists(dir_name):
#     shutil.rmtree(dir_name)

pattern = r" \((\d+)\)+\.txt$"


def get_file(current_path):
    dirs = listdir(current_path)

    if not path.exists(dir_name):
        os.makedirs(dir_name)

    for file in dirs:
        full_path = path.join(current_path, file)
        if full_path.endswith(".txt"):
            with open(path.join(dir_name, "path_date.txt"), 'a') as f:
                f.write(full_path + "\n")

            all_text_files_path = path.join(dir_name, "all_text_files")
            if not path.exists(all_text_files_path):
                os.makedirs(all_text_files_path)

            current_file = path.join(all_text_files_path, file)
            if path.exists(current_file):
                counter = 1
                file_name = file.replace(".txt", "")
                files = list(filter(lambda x: re.match(file_name + r" \(\d+\).txt", x), listdir(all_text_files_path)))
                files = list(map(lambda x: int(re.findall(pattern, x)[0]), files))

                counter = max(files) + 1 if len(files) > 0 else 1

                os.rename(current_file, current_file.replace(".txt", " ({}).txt".format(counter)))
            shutil.copy(full_path, all_text_files_path)
        else:
            get_file(full_path)

        # else:
        #     text_list.append(full_path)

    # shutil.copy([txt for txt in text_list],dirName)


get_file(r"C:\Users\a.zare\Desktop\data")
