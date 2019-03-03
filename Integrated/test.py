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
# import subprocess
# sample_ip = '52.109.60.3'
# command = ['python3','./IPGeoLocation-master/ipgeolocation.py','-t',sample_ip]
# p = subprocess.Popen(command, stdout=subprocess.PIPE)
# text = p.stdout.read()
# # text = text[len(text)-15:]
# text = text[-50:-1]
# temp = str(text)
# temp = list(temp)
# location = []
# flag = False
# comma = 0
# for i in range(0, len(temp)):
#     if temp[i] =='@' or comma <=2 and flag:
#         flag = True
#         location.append(temp[i])
#         if temp[i] == ',':
#             comma = comma+1
#             if comma == 2:
#                 break
# location = location[1:-1]
# location = ''.join(location)
# print(location)
# retcode = p.wait()
import requests
params = {'apikey': '838b800fcc312492d40b7a665447b6027823817ac272fc96b48c78a0b3436ccb', 'url': '132.145.34.87'}
response = requests.post('https://www.virustotal.com/vtapi/v2/url/scan', data=params)
json_response = response.json()
# print(json_response)
headers = {
  "Accept-Encoding": "gzip, deflate",
  "User-Agent" : "gzip,  My Python requests library example client or username"
  }
params = {'apikey': '838b800fcc312492d40b7a665447b6027823817ac272fc96b48c78a0b3436ccb', 'resource':'132.145.34.87'}
response = requests.post('https://www.virustotal.com/vtapi/v2/url/report',params=params, headers=headers)
json_response = response.json()
# print(json_response)


import csv
import requests
# File scanning
params = {'apikey': '838b800fcc312492d40b7a665447b6027823817ac272fc96b48c78a0b3436ccb'}
files = {'file': ('myfile.exe', open('../VT/myfile.exe', 'rb'))}
response = requests.post('https://www.virustotal.com/vtapi/v2/file/scan', files=files, params=params)
json_response = response.json()
json_response = dict(json_response)
resource = json_response['resource']

headers = {
  "Accept-Encoding": "gzip, deflate",
  "User-Agent" : "gzip,  My Python requests library example client or username"
  }
params = {'apikey': '838b800fcc312492d40b7a665447b6027823817ac272fc96b48c78a0b3436ccb', 'resource':resource}
response = requests.post('https://www.virustotal.com/vtapi/v2/file/report',params=params, headers=headers)
json_response = response.json()
result = dict(json_response)



with open('mycsvfile.csv', 'w') as f:  # Just use 'w' mode in 3.x
    w = csv.DictWriter(f, result.keys())
    w.writeheader()
    w.writerow(result)
