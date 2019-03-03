import walk
import os
import platform
import subprocess
directory = "/Users/ombahiwal/Documents/GitHub/sih-lambda-initial/Integrated/"
file_count = 0
for root, dirs, files in os.walk(directory):
    for file in files:
        file_count = file_count +1
        print("\nChecking : ", file, "in", directory)
        command = ['python3', 'malware-classification.py', directory+file]
        p = subprocess.Popen(command, stdout=subprocess.PIPE)
        text = p.stdout.read()
        retcode = p.wait()
        del p
