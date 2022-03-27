""" You must use this script by example 127.0.0.1 10000 1 """
from datetime import datetime
import socket
import threading
import sys

result = list()

def scan(ip, port, port_dict, delay):
    sp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(delay)
    
    try:
        sp.connect((ip, port))
        port_dict[port] = "open"
        sp.close()
    except:
        port_dict[port] = "close"
    
    result.append(port_dict)

def async_call(address_ip, ports, delay):
    port_dict = dict()
    count_open_port = 0
    time_start = datetime.timestamp(datetime.today())

    for port in range(ports):
        t = threading.Thread(target=scan, args=(address_ip, port, port_dict, delay))
        result.append(t)

    print("Loading............")

    for port in range(ports):
        result[port].start()

    for port in range(ports):
        result[port].join()
    
    for i in range(ports):
        if port_dict[i] == "open":
            print("Port {} is : {}".format(str(i), port_dict[i]))
            count_open_port += 1
    end_start = datetime.timestamp(datetime.today())
    print("Scan time: {} seconds".format(str(end_start - time_start).split(".")[0]))
    print("Scan result: {} are open and {} are close or filter".format(str(count_open_port), str(len(port_dict) - count_open_port)))
        
def main(address_ip, port, delay):
    """ This is main function we launch at begining of all """
    async_call(address_ip, port, delay)
    

if len(sys.argv) == 4:
    try:
        main(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
    except KeyboardInterrupt:
        print("Keyboard Interruption.\nBye")
        exit()
else:
    print("Error. You must use this script by example 127.0.0.1 10000 1")
    exit()

# time_start = datetime.timestamp(datetime.today())
# end_start = datetime.timestamp(datetime.today())
