import requests
import platform
import subprocess
import csv
import pickle
from ipwhois import IPWhois
import time, threading
import os
import signal

WAIT_SECONDS = 5
def gui_Call():
    gui_file = "../GUI Trials/FinalGUI.py"
    command = ['python3' , gui_file]
    p = subprocess.Popen(command, stdout=subprocess.PIPE)
    retcode = p.wait()
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

    # ip parsing logic - foriegn_ips
    foriegn_ips = []
    if operating_system == 'Darwin':
        for i in range(1, len(output_in_list)):
            temp = output_in_list[i][4].split(".")
            temp = temp[0:-1]
            temp = str.join('.', temp)
            foriegn_ips.append(temp)

    elif operating_system == 'Linux' or 'Windows':
        for i in range(1, len(output_in_list)-1):
            temp = output_in_list[i][4].split(".")
            temp2 = temp[-1]
            temp2 = temp2.split(':')
            temp = temp[0:-1]
            temp.append(temp2[0])
            temp = str.join('.', temp)
            foriegn_ips.append(temp)
    print("IP Parsing Done..")


    # # VT
    # if operating_system == 'Linux':
    #     try:
    #         output_in_list[0].append('VT result')
    #         for i in range(1, len(output_in_list)):
    #             if len(output_in_list[i][6].split('/')) == 2:
    #                 pid = (output_in_list[i][6].split('/'))[0]
    #                 command = ['python3', 'vt_file_scan.py', '-s', pid]
    #                 p = subprocess.Popen(command, stdout=subprocess.PIPE)
    #                 print("Loading...")
    #                 text = p.stdout.read()
    #                 print(text)
    #                 output_in_list[i].append(text)
    #                 r = requests.post(' https://iv7rvncxh7.execute-api.us-east-2.amazonaws.com/genysis/', json={"id": output_in_list[i][6], "Malicious": str(text)})
    #                 print(r.json())
    #                 # if text == 'None':
    #                 #     p = subprocess.Popen(command, stdout=subprocess.PIPE)
    #                 #     print("Loading ML...")
    #                 #     text = p.stdout.read()
    #                 retcode = p.wait()
    #     except:
    #         print("Some error Occured in VT")
    # Code for IP Location

    # output_in_list[0].append('Location')
    # for i in range(0, len(foriegn_ips)):
    #     command = ['python3','./IPGeoLocation-master/ipgeolocation.py','-t',foriegn_ips[i]]
    #     p = subprocess.Popen(command, stdout=subprocess.PIPE)
    #     text = p.stdout.read()
    #     # text = text[len(text)-15:]
    #     text = text[-25:-10]
    #     temp = str(text)
    #     temp = temp[2:-1]
    #     output_in_list[i+1].append(temp)
    #     retcode = p.wait()


    # sample_ip = output_in_list[1][4]
    # sample_ip = '52.109.60.3'
    # command = ['../Scripts/for_maps/IPGeoLocation-master/./ipgeolocation.py','-t',sample_ip]
    # p = subprocess.Popen(command, stdout=subprocess.PIPE)
    # text = p.stdout.read()
    # # print(text)
    # retcode = p.wait()

    # python3 filename.py -f inputfile.txt -c outputfile.csv



    # GEOLocation Lookup

    print("Finding IP Geo locations...")
    locations = []
    command = ['python3','./IPGeoLocation-master/ipgeolocation.py','-m']
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
            if temp[i] == ',':
                comma = comma+1
                if comma == 2:
                    break
            flag = True
            location.append(temp[i+1])

    location = location[1:-1]
    location = ''.join(location)
    locations.append(location)
    retcode = p.wait()

    output_in_list[0].append('Location')
    for j in range(0, len(foriegn_ips)):
        command = ['python3','./IPGeoLocation-master/ipgeolocation.py','-t',foriegn_ips[j]]
        p = subprocess.Popen(command, stdout=subprocess.PIPE)
        text = p.stdout.read()
        # text = text[len(text)-15:]
        text = text[-50:-1]
        # print(text)/
        temp = str(text)
        temp = list(temp)
        location = []
        flag = False
        comma = 0
        for i in range(0, len(temp)):
            if temp[i] =='@' or comma <=2 and flag:
                if temp[i] == ',':
                    comma = comma+1
                    if comma == 2:
                        break
                flag = True
                location.append(temp[i])

        location = location[1:-1]
        location = ''.join(location)
        locations.append(location)
        output_in_list[j+1].append(location)
        retcode = p.wait()
    print("Geolocations found..")


# Write Basemap CSV File

    for i in range(0, len(locations)):
        temp = locations[i].split(',')
        locations[i] = temp
        # By default safe
        locations[i].append(1)

    with open("basemap_locations.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows(locations)
        print("File write Done.. \nsaved as basemap_locations.csv")
    print("Basemap file Generated..")

    # abuse IP Code
    output_in_list[0].append('AbuseIP ConScore')
    print("Abuse IP test Running...")
    # print(foriegn_ips)
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


    #code for country lookup
    print("whois country lookup...")
    output_in_list[0].append('Country')
    output_in_list[0].append('ASN Description')
    for i in range(0, len(foriegn_ips)):

        try:
            obj = IPWhois(foriegn_ips[i])
            results = obj.lookup_whois()
            output_in_list[i+1].append(results['nets'][0]['country'])
            output_in_list[i+1].append(results['asn_description'] )
        except:
            print("Private connection found at ",foriegn_ips[i] )
            output_in_list[i+1].append('-local-')
            output_in_list[i+1].append('-local-')
    print("Country Lookup Done..")

        # Logic to write the data into a file
    with open("main_output.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows(output_in_list)
        # print(output_in_list)
        print("File write Done.. \nsaved as main_output.csv")
    print("Test Finished.\nGenysis NAT")
    threading.Timer(WAIT_SECONDS, foo).start()
gui_Call()
foo()




def kill_process(pid):
    try:
        os.kill(pid, signal.SIGTERM)
        print("Process - ",pid, "Terminated!")
    except:
        print("Could Not terminate process -",pid)
