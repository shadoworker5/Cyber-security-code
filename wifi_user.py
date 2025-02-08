import subprocess
import re as regex
import socket
from datetime import datetime
from threading import Thread, enumerate as thread_enumerate, current_thread as thread_current
import argparse
from ipaddress import ip_address

hosts       = []
found_hosts = []
RED         = '\033[31m'
GREEN       = '\033[32m'

def generateIPList(host, start, end):
    split_host_ip = host.split('.')
    for i in range(start, end + 1):
        tmp_end = int(split_host_ip[3]) + i
        if tmp_end <= 255:
            new_ip  = f'{split_host_ip[0]}.{split_host_ip[1]}.{split_host_ip[2]}.{tmp_end}'
            hosts.append(new_ip)

def getUserNameByIP(ip):
    name = ''
    try:
        hosname, __, ___ = socket.gethostbyaddr(ip)
        name = hosname
    except:
        name = 'Not found'
    return name

def sendPingQuery(host):
    command     = subprocess.Popen(f'ping {host} -c 5', shell=True, stdout=subprocess.PIPE, text=True)
    result, _   = command.communicate()
    
    if regex.search('Request timeout for icmp_seq 3', result) or regex.search('Host is down', result):
        print(f'{host} not found')
    else:
        print(f'{host} found')
        found_hosts.append(host)

def pingRequest():
    for host in hosts:
        t = Thread(target=sendPingQuery, args=(host,))
        t.start()
    
    for thread in thread_enumerate():
        if thread != thread_current():
            thread.join()

def isOpenPort(host, start_port, end_port):
    for port in range(start_port, end_port + 1):
        command     = subprocess.Popen(f'nc -vz {host} {port}', shell=True, stdout=subprocess.PIPE, text=True)
        result, _   = command.communicate()
        
        if regex.search('Connection refused', result):
            print(f'{port} on {host} is close')
        else:
            print(f'{port} is open')
            found_hosts.append({host: {port: 'is open'}})

def getHostIP():
    host_ip = '127.0.0.1'
    try:
        host_name   = socket.gethostname()
        host_ip     = socket.gethostbyname(host_name)
    except Exception as e:
        print(f'error occur in getHostIP: {str(e)}')
    return host_ip

def main(address_ip, start_ip, end_ip):
    """ This is main function we launch at begining of all """
    time_start  = datetime.timestamp(datetime.today())
    size_name   = 34
    size_host   = 18
    generateIPList(address_ip, start_ip, end_ip)
    pingRequest()

    print('\n\n')
    print('-'*60)
    print(f'| Address Ip {" "*8} | Host name {" ":<24} |')
    print('-'*60)
    
    for host in found_hosts:
        host_name   = getUserNameByIP(host)
        tab_size    = size_name - len(host_name)
        host_size   = size_host - len(host)
        print(f'| {host} {" "*host_size} | {host_name}{" "*tab_size} |')

    if len(found_hosts) > 0: print('-'*60)
    
    end_start = datetime.timestamp(datetime.today())
    print('\n\nScan time: {} seconds'.format(str(end_start - time_start).split(".")[0]))

if __name__ == '__main__':
    try:
        banner = '''
        __        __ ___  _____  ___   _   _  ____   _____  ____  
        \ \      / /|_ _||  ___||_ _| | | | |/ ___| | ____||  _ \ 
         \ \ /\ / /  | | | |_    | |  | | | |\___ \ |  _|  | |_) |
          \ V  V /   | | |  _|   | |  | |_| | ___) || |___ |  _ < 
           \_/\_/   |___||_|    |___|  \___/ |____/ |_____||_| \_\\
        '''
        
        print(RED)
        print(banner)
        print(GREEN)
        
        parser = argparse.ArgumentParser()
        parser.add_argument('-o', '--own', help='Analyze your own local connexion', action='store_true')
        parser.add_argument('-t', '--target', help='Analyze your target connexion')
        parser.add_argument('-s', '--start', help='First addresse to analyze', type=int, default=1)
        parser.add_argument('-e', '--end', help='Last addresse to analyze', type=int, default=255)
        args = parser.parse_args()

        if args.target:
            target_ip = args.target
            result = ip_address(target_ip)
            main(result, args.start, args.end)
        elif args.own:
            host_ip = getHostIP()
            main(host_ip, args.start, args.end)
        else:
            parser.print_help()
    except Exception as e:
        print('Keyboard Interruption.\nBye')
        exit(0)