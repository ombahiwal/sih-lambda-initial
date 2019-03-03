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

super_list = []


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




"""def get_report():
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
                    print("0")
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
                    print("0")
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
"""

def main():

    list1 = []
    str1 = args.string
    list1 = str1.split(',')[0]
    super_list = list1
    print(list1)

if __name__ == '__main__':
    main()
