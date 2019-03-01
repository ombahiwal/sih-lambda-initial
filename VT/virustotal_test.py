# import requests
#
# params = {'apikey': '838b800fcc312492d40b7a665447b6027823817ac272fc96b48c78a0b3436ccb', 'url': '157.33.231.212'}
# response = requests.post('https://www.virustotal.com/vtapi/v2/url/scan', data=params)
# json_response = response.json()
#
# print json_response
#
#
# headers = {
#   "Accept-Encoding": "gzip, deflate",
#   "User-Agent" : "gzip,  My Python requests library example client or username"
#   }
# params = {'apikey': '838b800fcc312492d40b7a665447b6027823817ac272fc96b48c78a0b3436ccb', 'resource':'http://www.virustotal.com'}
# response = requests.post('https://www.virustotal.com/vtapi/v2/url/report',
#   params=params, headers=headers)
# json_response = response.json()


# var = os.system("netstat -lntu")
# import os
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
text = p.stdout.read()
# output fetched in the "Text" Variable as a string, later data can be extracted with regular expressions.
# one = line by line
one = list(text.decode().split("\n"))
output_in_list = []

# Get Column Names
two = one[3].split(" ")
output_in_list = []
three = []
two = one[1]
two = two.split("  ")
temp = two[1:]
two = two[0].split(" ")
two.extend(temp)

for j in range(1, len(one)):
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
with open("main_output.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(output_in_list)

print(output_in_list)
p.kill()
retcode = p.wait()
