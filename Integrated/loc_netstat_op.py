import platform
import subprocess
print("All Listening Ports: ")
operating_system = platform.system()
command_win = ['netstat', '-ab']
command_linux = ['netstat', '-tup']
command_mac = ['netstat', '-p', 'tcp']
if operating_system == 'Darwin':
    command = command_mac
elif operating_system == 'Linux':
    command = command_linux
elif operating_system == 'Windows':
    command = command_win

p = subprocess.Popen(command, stdout=subprocess.PIPE)
text = p.stdout.read()
# output fetched in the "Text" Variable as a string, later data can be extracted with regular expressions.
# one = line by line
one = list(text.decode().split("\n"))
#
two = one[3].split(" ")
output_in_list = []
for j in range(2, len(one)):
    three = []
    two = one[j].split(" ")
    for i in range(0, len(two)):
        if two[i] != '':
            three.append(two[i])
    output_in_list.append(three)
del one
del two
del three
del text

print(output_in_list)
p.kill()
retcode = p.wait()
