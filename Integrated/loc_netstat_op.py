import platform
import subprocess
import csv
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
print(temp)
temp2 = []
for i in range(0, len(temp)):
    if temp[i] != '':
        temp2.append(temp[i])
two = two[0].split(" ")
print(two)
print(temp2)
two.extend(temp2)
temp2 = two
output_in_list = []

for j in range(1, len(one)):
    three = []
    two = one[j].split(" ")
    for i in range(0, len(two)):
        if two[i] != '':
            three.append(two[i])
    output_in_list.append(three)

output_in_list[0] = temp2
del one
del two
del three
del text
print("Netstat Done..")
with open("main_output.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(output_in_list)

print(output_in_list)
print("File write Done.. saved as main_output.csv")
retcode = p.wait()
