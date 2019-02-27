#!/bin/bash

sudo netstat -tn | awk '/EST/{print $5}' | sed 's/:.*//' | 
    while read ip; do 
	echo $ip;
        python3 ipgeolocation.py -t $ip | grep "Latitude\|Longtitude\|ISP" ;
    done
