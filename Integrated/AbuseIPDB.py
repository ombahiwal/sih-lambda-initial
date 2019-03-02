#! /bin/python/env
import argparse
import codecs
import csv
import ipaddress
import json
import os.path
import re
import socket
import sys
import time

import requests

api_key = 'Z1vdRXc5r21VM0qTOiIdrT20U1aivVoxAj5ejyvw'

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
    "-i",
    "--ip",
    help="Takes a single IP Addresse",
    action="store")

# Outputs
parser.add_argument(
    "-c", "--csv", help="outputs items in comma seperated values",  action="store")
parser.add_argument(
    "-j", "--json", help="outputs items in jsonl format",  action="store")
parser.add_argument(
    "-l", "--jsonl", help="outputs items in jsonl format",  action="store")
parser.add_argument(
    "-t", "--tsv", help="outputs items in tab seperated values (Default)", action="store")

# Additional Options
parser.add_argument(
    "-d", "--days", help="take in the number of days in history to go back for IP reports. Default: 30 Days", type=int)
parser.add_argument("-x", "--translate",
                    help="By default categories are numbers, with this flag it will convert them to text",  action="store_true")
parser.add_argument("-v", "--version', action='version', version='%(prog)s 2.0")

logs = []
args = parser.parse_args()


def get_file(infile):
    with codecs.open(infile, "r", encoding='utf-8', errors='ignore') as f:
        return f.read()


def get_cat(x):
    return {
        3: 'Frad_Orders',
        4: 'DDoS_Attack',
        5: 'FTP_Brute-Force',
        6: 'Ping of Death',
        7: 'Phishing',
        8: 'Fraud VoIP',
        9: 'Open_Proxy',
        10: 'Web_Spam',
        11: 'Email_Spam',
        12: 'Blog_Spam',
        13: 'VPN IP',
        14: 'Port_Scan',
        15: 'Hacking',
        16: 'SQL Injection',
        17: 'Spoofing',
        18: 'Brute_Force',
        19: 'Bad_Web_Bot',
        20: 'Exploited_Host',
        21: 'Web_App_Attack',
        22: 'SSH',
        23: 'IoT_Targeted',
    }.get(
        x,
        'UNK CAT, ***REPORT TO MAINTAINER***OPEN AN ISSUE ON GITHUB w/ IP***')


def abuse_check(IP, days):
    request = 'https://www.abuseipdb.com/check/%s/json?key=%s&days=%s' % (IP, api_key, days)
    # DEBUG
    # print(request)
    r = requests.get(request)
    # DEBUG
    # print(r.json())
    data = r.json()
    if not data:
        logs.append({'ip': IP, 'category': [], 'created': '', 'country': '','isoCode': '', 'isWhitelisted': False, 'abuseConfidenceScore': 0})
    elif type(data) is list:
        for record in data:
            logs.append(record)
    else:
        logs.append(data)


def get_report():
    log_check = None
    # Convert category numbers to words
    if args.translate:
        for log in logs:
            tmp_catergory = []
            category = log['category']
            for cat in category:
                tmp_catergory.append(get_cat(cat))
            log['category'] = tmp_catergory

    # Output options
    if args.csv:
        keys = logs[0].keys()
        with open(args.csv, 'w') as outfile:
            dict_writer = csv.DictWriter(outfile, keys)
            dict_writer.writeheader()
            dict_writer.writerows(logs)
        pass
    elif args.tsv:
        keys = logs[0].keys()
        with open(args.tsv, 'w') as outfile:
            dict_writer = csv.DictWriter(outfile, keys, delimiter='\t')
            dict_writer.writeheader()
            dict_writer.writerows(logs)
        pass
    elif args.jsonl:
        json_logs = json.dumps(logs)
        with open(args.jsonl, 'w') as outfile:
            for log in logs:
                json.dump(log, outfile)
                outfile.write('\n')
        pass
    elif args.json:
        with open(args.json, 'w') as outfile:
            json.dump(logs, outfile)
        pass
    else:
        for log in logs:
            #print(log)
            list2 = []
            if (log_check == None):
                list2 = [log["ip"],log["category"],log['country'],log["isoCode"],log["abuseConfidenceScore"],log['isWhitelisted']]
                if (log['isWhitelisted'] == True):
                    print("0",)
                    with open('example_output.csv', 'a', newline='') as csvfile3:
                        writer = csv.writer(csvfile3)
                        writer.writerows([list2])
                    with open('white_listed.csv', 'a', newline='') as csvfile4:
                        writer = csv.writer(csvfile4)
                        writer.writerows(list2)
                else:
                    print(log["abuseConfidenceScore"])
                    with open('example_output.csv', 'a', newline='') as csvfile5:
                        writer = csv.writer(csvfile5)
                        writer.writerows([list2])
                    with open('black_listed.csv', 'a', newline='') as csvfile6:
                        writer = csv.writer(csvfile6)
                        writer.writerows([list2])
            elif (log['ip'] == log_check):
                pass
            else:
                list2 = [log["ip"],log["category"],log['country'],log["isoCode"],log["abuseConfidenceScore"],log['isWhitelisted']]
                if(log['isWhitelisted'] == True):
                    print("0","")
                    with open('example_output.csv', 'a', newline='') as csvfile3:
                        writer = csv.writer(csvfile3)
                        writer.writerows([list2])
                    with open('white_listed.csv', 'a', newline='') as csvfile4:
                        writer = csv.writer(csvfile4)
                        writer.writerows([list2])
                else:
                    print(log["abuseConfidenceScore"])
                    with open('example_output.csv', 'a', newline='') as csvfile5:
                        writer = csv.writer(csvfile5)
                        writer.writerows([list2])
                    with open('black_listed.csv', 'a', newline='') as csvfile6:
                        writer = csv.writer(csvfile6)
                        writer.writerows([list2])
            log_check = log['ip']
        pass


def main() :
    check_ip = 0
    data_ip = None
    if args.days:
        days = args.days
    else:
        days = 30

    if args.file:
        f = get_file(args.file)
        found = re.findall(
            r'(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})', f)

        list(found)

        count = 0
        for ip in found:
            try:
                socket.inet_aton(ip)
                pass
            except socket.error:
                continue

            if ipaddress.ip_address(ip).is_private is False:
                if count == 59:
                    time.sleep(60)
                    count = 0
                abuse_check(ip, days)
                count += 1
        get_report()
    elif args.ip:
        c_ip = args.ip
        if ipaddress.ip_address(args.ip).is_private is False:
            if os.path.exists('example_output.csv') is True:
                with open('example_output.csv', 'r') as csvfile1:
                    csvreader = csv.reader(csvfile1)
                    list1 = list(csvreader)
                for i in range(len(list1)):
                    #print(len(list1))
                    if list1[i][0] == args.ip:
                        #print("-------------------------------")
                        check_ip = 1
                        if list1[i][5] == True:
                            data_ip=0
                        else:
                            data_ip=list1[i][4]
                    else:
                        pass
                if check_ip != 1:
                    #print("calling abuse_check")
                    abuse_check(c_ip, days)
                    get_report()
                else:
                    print(data_ip)
            else:
                    #with open('example_output.csv', 'w') as csvfile2:
                    #csvfile2.close()
                abuse_check(args.ip, days)
                get_report()
        else:
            sys.exit("A Private IP will return no result...")
    else:
        sys.exit(
            "error: one of the following arguments are required: -f/--file or -i/--ip")


if __name__ == '__main__':
    main()
