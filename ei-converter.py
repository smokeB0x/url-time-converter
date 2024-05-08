# -*- coding: utf-8 -*-
"""
Script to convert ei-value in google search URLs to human readable timestamps.
Based on the python2 script written by Adrian Leong (cheeky4n6monkey@gmail.com)
https://github.com/cheeky4n6monkey/4n6-scripts/blob/master/utilities/google-ei-time.py

"""
import sys
import base64
import datetime

if len(sys.argv) > 1:
    value = sys.argv[1]  
else:
    print("No input string provided.")
    print("Usage: python3 ei-converter.py <ei-value>")


print("Inputed value: ", value)

num_extra_bytes = (len(value) % 4) 
if (num_extra_bytes != 0):
    padlength = 4 - num_extra_bytes 
    padstring = value + padlength*'='
else:
    padstring = value

print("Padded base64 string = " + padstring)

decoded = base64.urlsafe_b64decode(padstring)

timestamp = decoded[0] + decoded[1]*256 + decoded[2]*(256**2) + decoded[3]*(256**3)

print("Timestamp: ", timestamp)

datetimestr = datetime.datetime.utcfromtimestamp(timestamp).strftime('%d-%m-%Y T%H:%M:%S UTC')

print("Date and time: ", datetimestr)


