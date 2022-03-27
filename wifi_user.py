import subprocess
import re as regex
import socket
import sys
from datetime import datetime

hosts = []

# Get username by ip address
def get_user_name(ip):
    try:
        name, other, host_ip = socket.gethostbyaddr(ip)
        return name
    except:
        return "Not found"

# Send ping request to check all address use in this network
def ping_request(host, start_ip, end_ip):
    for i in range(start_ip, end_ip):
        command = subprocess.Popen("ping "+ host[0:-1]+str(i) +" -n 2", shell=True, stdout=subprocess.PIPE, text=True)
        result, erreur = command.communicate()
        if regex.search(" Impossible de joindre l'h“te de destination.", result) == None:
            hosts.append(host[0:-1]+str(i))
            print("{} found".format(host[0:-1]+str(i)))

# This function is use to get user input
def get_input(input_type, msg):
    result = ""
    while True:
        try:
            response = input_type(input(msg))
        except:
            continue

        if input_type == str:
            if regex.match(r"^1[0-9]{1,2}([.]?[0-9]{1,3}){3}$", response):
                result = response
                break
        elif input_type == int:
            result = response
            break
    return result

# This function the start point of this script
def main(address_ip, start_ip, end_ip):
    """ This is main function we launch at begining of all """
    time_start = datetime.timestamp(datetime.today())
    ping_request(address_ip, start_ip, end_ip)

    print("-"*25)
    print("Address Ip   | Host name")
    print("-"*25)
    
    for host in hosts:
        name = get_user_name(host)
        print("{}    | {}".format(host, name))
    
    end_start = datetime.timestamp(datetime.today())
    print("Scan time: {} seconds".format(str(end_start - time_start).split(".")[0]))

if len(sys.argv) == 4:
    try:
        main(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
    except KeyboardInterrupt:
        print("Keyboard Interruption.\nBye")
        exit()
else:
    print("Error. You must use this script by example 127.0.0.1 1 255")
    exit()