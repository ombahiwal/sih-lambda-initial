import platform
import subprocess
import csv
import pickle
from ipwhois import IPWhois
import time, threading

WAIT_SECONDS = 5

def foo():
    print('*GENYSIS NAT*\n--- Executing Main Loop Thread --- ')
    print(time.ctime())
    print("LISTING OPEN PORTS: ")
    operating_system = platform.system()
    command_win = ['netstat', '-n']
    command_linux = ['netstat', '-tupn']
    command_mac = ['netstat', '-p', 'tcp', '-n']
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
    # Get Column Namess
    two = one[3].split(" ")
    three = []
    two = one[1]
    two = two.split("  ")
    temp = two[1:]
    temp2 = []
    for i in range(0, len(temp)):
        if temp[i] != '':
            temp2.append(temp[i])
    two = two[0].split(" ")
    two.extend(temp2)
    temp2 = two
    #column anomanly for darwin
    if operating_system != 'Darwin':
        test = str(temp2[3]+" "+ temp2[4])
        del temp2[4]
        temp2[3] = test
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

    output_in_list.pop()
    length_output = len(output_in_list)

    print("Netstat Done..")

    retcode = p.wait()



    # Code for IP Location

    # sample_ip = output_in_list[1][4]
    # sample_ip = '52.109.60.3'
    # command = ['../Scripts/for_maps/IPGeoLocation-master/./ipgeolocation.py','-t',sample_ip]
    # p = subprocess.Popen(command, stdout=subprocess.PIPE)
    # text = p.stdout.read()
    # # print(text)
    # retcode = p.wait()

    # python3 filename.py -f inputfile.txt -c outputfile.csv

    # ip parsing logic - foriegn_ips
    foriegn_ips = []
    if operating_system == 'Darwin':
        for i in range(1, len(output_in_list)):
            temp = output_in_list[i][4].split(".")
            temp = temp[0:-1]
            temp = str.join('.', temp)
            foriegn_ips.append(temp)

    elif operating_system == 'Linux':
        for i in range(1, len(output_in_list)-1):
            temp = output_in_list[1][4].split(".")
            temp2 = temp[-1]
            temp2 = temp2.split(':')
            temp = temp[0:-1]
            temp.append(temp2[0])
            temp = str.join('.', temp)
            foriegn_ips.append(temp)
    print("IP Parsing Done..")

    #code for country lookup
    print("whois country lookup...")
    output_in_list[0].append('Country')
    for i in range(0, len(foriegn_ips)):
        obj = IPWhois(foriegn_ips[i])
        results = obj.lookup_whois()
        output_in_list[i+1].append(results['nets'][0]['country'])
    print("Country Lookup Done..")


    # Abuse IP Logic
    output_in_list[0].append('AbuseIP ConScore')
    print("Abuse IP test Running...")
    for i in range(0, len(foriegn_ips)):
        print("Testing : ",foriegn_ips[i])
        command = ['python3' , 'AbuseIPDB.py','-i',foriegn_ips[i]]
        p = subprocess.Popen(command, stdout=subprocess.PIPE)
        text = p.stdout.read()
        output_in_list[i+1].append(str(text))
        retcode = p.wait()
    for i in range(1, length_output):
        temp = output_in_list[i][-1]
        temp = temp[:-3]
        temp = temp[2:]
        output_in_list[i][-1] = temp

    threading.Timer(WAIT_SECONDS, foo).start()
        # Logic to write the data into a file
    with open("main_output.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows(output_in_list)
        # print(output_in_list)
        print("File write Done.. saved as main_output.csv")
    print("Test Finished.\nGenysis NAT")
foo()
