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

def main():

    list1 = []
    str1 = args.string
    list1 = str1.split(',')[0]
    super_list = list1
    print(list1)

if __name__ == '__main__':
    main()
