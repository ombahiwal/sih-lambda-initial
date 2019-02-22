# Dependency is subprocess, do pip install subprocess before executing
import subprocess
print("All Listening Ports: ")
command = ['netstat', '-lntu']
p = subprocess.Popen(command, stdout=subprocess.PIPE)
text = p.stdout.read()
# output fetched in the "Text" Variable as a string, later data can be extracted with regular expressions.
print text
retcode = p.wait()
