# import platform
# import subprocess
# command = ['netstat', '-p', 'tcp', '-n']
# p = subprocess.Popen(command, stdout=subprocess.PIPE)
# print("Loading...")
# text = p.stdout.read()
# # output fetched in the "Text" Variable as a string, later data can be extracted with regular expressions.
# # one = line by line
# one = list(text.decode().split("\n"))
# # Get Column Names
# two = one[3].split(" ")
# three = []
# two = one[1]
# two = two.split("  ")
# temp = two[1:]
# temp2 = []
# print(temp)
# retcode = p.wait()

# Code for IP Location

# sample_ip = output_in_list[1][4]
import subprocess
sample_ip = '52.109.60.3'
command = ['python3','./IPGeoLocation-master/ipgeolocation.py','-t',sample_ip]
p = subprocess.Popen(command, stdout=subprocess.PIPE)
text = p.stdout.read()
# text = text[len(text)-15:]
text = text[-50:-1]
temp = str(text)
temp = list(temp)
location = []
flag = False
comma = 0
for i in range(0, len(temp)):
    if temp[i] =='@' or comma <=2 and flag:
        flag = True
        location.append(temp[i])
        if temp[i] == ',':
            comma = comma+1
            if comma == 2:
                break
location = location[1:-1]
location = ''.join(location)
print(location)
retcode = p.wait()
