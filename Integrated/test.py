import platform
import subprocess
command = ['netstat', '-p', 'tcp', '-n']
p = subprocess.Popen(command, stdout=subprocess.PIPE)
print("Loading...")
text = p.stdout.read()
# output fetched in the "Text" Variable as a string, later data can be extracted with regular expressions.
# one = line by line
one = list(text.decode().split("\n"))
# Get Column Names
two = one[3].split(" ")
three = []
two = one[1]
two = two.split("  ")
temp = two[1:]
temp2 = []
print(temp)
retcode = p.wait()
