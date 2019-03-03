import requests
import csv
import os
import argparse
import subprocess
from pprint import pprint
super_list = []

def main():
    list1 = []
    output_in_list = []
    str1 = args.string
    command = ['ps', str1]
    super_list = str1
    p = subprocess.Popen(command, stdout=subprocess.PIPE)
    # print("Loading...")
    text = p.stdout.read()
    # output fetched in the "Text" Variable as a string, later data can be extracted with regular expressions.
    # one = line by line
    one = list(text.decode().split("\n"))
    # Get Column Namess
    # print((one[1].split(' '))[-1])
    retcode = p.wait()
    # Virus Total
    # print("Virus Total File Check")
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
    # pprint(result)
    try:
        print(result['scans']['Bkav']['detected'])
        with open('virustotal.csv', 'w') as file2:  # Just use 'w' mode in 3.x
            w = csv.DictWriter(file2, result.keys())
            w.writeheader()
            w.writerow(result)
        # print("VT csv file generated...virustotal.csv")
    except:
        print("Couldnt generate VT CSV file..")



# # 7376



parser = argparse.ArgumentParser(
    description='This program utilizes the Abuse IP Database from: AbuseIPDB.com to perform queries about IP addresses and returns the output to standard out.'
)
required = parser.add_mutually_exclusive_group()
required.add_argument(
    "-f",
    "--file",
    help="parses IP Addresses from a single given file",
    action="store")
required.add_argument(
    "-s",
    "--string",
    help="Takes a single IP Addresse",
    action="store")

logs = []
args = parser.parse_args()


def get_file(infile):
    with codecs.open(infile, "r", encoding='utf-8', errors='ignore') as f:
        return f.read()

if __name__ == '__main__':
    super_list= ''
    main()


# list_of_dir = os.listdir("./")

# for i in range(0, len(list_of_dir))

# save virustotal report

#
