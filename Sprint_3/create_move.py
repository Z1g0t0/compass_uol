import os
import shutil
import subprocess

files_path = 'D:/Documents/Compass_uol/Sprint_3/'

for filename in os.listdir(files_path):
    #breakpoint()
    file_path = files_path + filename

    if filename.startswith("Ex_") and os.path.isfile(file_path):
        dir_path = file_path[:-3]

        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        shutil.move(file_path, dir_path)

        