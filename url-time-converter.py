# -*- coding: utf-8 -*-
"""
Script to decode certain values in URLs into date and time of posting. 
The values need to be manually extracted from the URL and inputed into the CLI
Version: 1.0
"""
import sys
import base64
import datetime

def main():
    if len(sys.argv) != 3:
        print("Error! wrong input.")
        print("Usage: python3 url-time-converter.py <option> <value>")
        print("Options:")
        print("-g = google ei-value")
        print("-t = tiktok value")
        sys.exit(1)
        
    option, value = sys.argv[1], sys.argv[2]
    
    if option == "-g":
        google_ei(value)
    elif option == "-t":
        try:
            tiktok_time(int(value))
        except ValueError:
            print("Error! Tiktok value must be numbers only (integer)")
            sys.exit(1)
    else:
        print("Error! wrong input.")
        print("Usage: python3 url-time-converter.py <option> <value>")
        print("Options:")
        print("-g = google ei-value")
        print("-t = tiktok value")
        sys.exit(1)
    
def google_ei(ei_value):
    '''
    Function to decode the ei-value in google search URLs to human readable timestamps.
    Based on the python2 script written by Adrian Leong (cheeky4n6monkey@gmail.com)
    https://github.com/cheeky4n6monkey/4n6-scripts/blob/master/utilities/google-ei-time.py
    '''
    print("Type of value: Google ei")
    print("Inputed value: ", ei_value)

    #The base64 value must be divisable by 4. This adds "=" until it is.
    num_extra_bytes = (len(ei_value) % 4) 
    if (num_extra_bytes != 0):
        padlength = 4 - num_extra_bytes 
        padstring = ei_value + padlength*'='
    else:
        padstring = ei_value
    
    print("Padded base64 string: " + padstring)

    #Decodes the urlsafe base64 string into bytes
    decoded = base64.urlsafe_b64decode(padstring)

    #Takes the first four bytes and interprets them as little endian, then converts them to decimal
    timestamp = decoded[0] + decoded[1]*256 + decoded[2]*(256**2) + decoded[3]*(256**3)
    
    print("Timestamp: ", timestamp)

    #Converts the timestamp to human readable date and time
    datetimestr = datetime.datetime.utcfromtimestamp(timestamp).strftime('%d-%m-%Y T%H:%M:%S UTC')
    
    print("Date and time: ", datetimestr)
    
def tiktok_time(tiktok_value):
    '''
    Function to decode the tiktok timestamp value found in tiktok URLs
    Note: This may work on URLs from other sites aswell, as e.g. linkedin
    '''
    print("Type of value: Tiktok")
    print("Inputed value: ", tiktok_value)
    
    #convert the int string to binary and remove the start (0b)
    binary_value = bin(tiktok_value)[2:]
    
    #Select the 31 first bits
    #31 because python removes leading "0". Its is actually the first 32 bits with the leading "0"
    first_31_bits = binary_value[:31]
    
    #Convert the binary bits into decimal
    timestamp = int(first_31_bits, 2)
    
    print("Timestamp: ", timestamp)
    
    #Convert the timestamp to human readable time
    datetimestr = datetime.datetime.utcfromtimestamp(timestamp).strftime('%d-%m-%Y T%H:%M:%S UTC')
    
    print("Date and time: ", datetimestr)
    

if __name__ == '__main__':
    main()

