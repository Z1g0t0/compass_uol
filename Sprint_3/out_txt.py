import os
import subprocess

files_path = 'D:/Documents/REPOS/Compass_UOL/Sprints/Sprint_3/'

for filename in os.listdir(files_path):

    #breakpoint()
    if filename.endswith(".py"):
        with open(filename[:-3] + ".txt", "wb") as output:
            with subprocess.Popen(args=["python", files_path + filename], stdout=subprocess.PIPE) as script:
                output.write(script.stdout.read())
        output.close()
    
