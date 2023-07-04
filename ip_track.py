"""
 * @author Shadoworker5 Dev
 * @email shadoworker5.dev@gmail.com
 * @create date 2022-09-14 23:37:22
 * @modify date 2023-07-04 11:22:39
 * @desc [description]
"""
import argparse
from socket import gethostbyaddr
import requests
from os import system, name as sys_name

API_TOKEN   = {"IPStack": "YOUR_TOKEN"}
RED         = '\033[31m'
GREEN       = '\033[32m'
WHITE       = '\033[0m' 
VERSION     = '1.0.1'

def localiseIP(ip):
    api_ipstack = f"http://api.ipstack.com/{ip}?access_key={API_TOKEN['IPStack']}"
    api_ipwhois = f'https://ipwhois.app/json/{ip}'
    try:
        response = requests.get(api_ipstack)
        if response.status_code == 200:
            response    = response.json()
            fai         = requests.get(f'{api_ipwhois}').json()
            map_url     = f"https://maps.google.com/?q={response['latitude']},{response['longitude']}"
            print(f"Target public IP: {response['ip']}")
            print(f"Type address    : {response['type']}")
            print(f"Continent code  : {response['continent_code']}")
            print(f"Continent name  : {response['continent_name']}")
            print(f"Country code    : {response['country_code']}")
            print(f"Country name    : {GREEN}{response['country_name']}{GREEN}")
            print(f"Region code     : {GREEN}{response['region_code']}{GREEN}")
            print(f"Region name     : {GREEN}{response['region_name']}{GREEN}")
            print(f"City            : {GREEN}{response['city']}{GREEN}")
            print(f"FAI             : {fai['org']}")
            print(f"Map Url         : {GREEN}{map_url}{GREEN}")
            print(f"Capital         : {response['location']['capital']}")
            print(f"Code languages  : {response['location']['languages'][0]['code']}")
            print(f"Name languages  : {response['location']['languages'][0]['name']}")
            print(f"Native languages: {response['location']['languages'][0]['native']}")
            print(f"Calling code    : {response['location']['calling_code']}")
            print(f"Country flag    : {response['location']['country_flag']}")
    except Exception as e:
        result = requests.get(api_ipwhois)
        if result.status_code == 200:
            result  = result.json()
            map_url = f"https://maps.google.com/?q={result['latitude']},{result['longitude']}"
            print(f"Target public IP: {result['ip']}")
            print(f"Type address    : {result['type']}")
            print(f"Continent code  : {result['continent_code']}")
            print(f"Continent name  : {result['continent']}")
            print(f"Country code    : {result['country_code']}")
            print(f"Country name    : {GREEN}{result['country']}{GREEN}")
            print(f"Region name     : {GREEN}{result['region']}{GREEN}")
            print(f"City            : {GREEN}{result['city']}{GREEN}")
            print(f"FAI             : {result['org']}")
            print(f"Maps Url        : {GREEN}{map_url}{GREEN}")
            print(f"Capital         : {result['country_capital']}")
            print(f"Borders         : {result['country_neighbours']}")
            print(f"Calling code    : {result['country_phone']}")
            print(f"Country flag    : {result['country_flag']}")
            print(f"Local currency  : {result['currency']}")
            print(f"Code currency   : {result['currency_code']}")
            print(f"Currency rates  : {result['currency_rates']}")
            print(f"Currency plural : {result['currency_plural']}")

def getHostIP():
    ip = ''
    try:
        response    = requests.get('https://api64.ipify.org?format=json').json()
        ip          = response["ip"]
    except Exception as e:
        ip = '127.0.0.1'
    return ip
    
def getHostName(ip):
    host_name, _, t_ip = gethostbyaddr(ip)
    return host_name

def getTargetIP():
    from ipaddress import ip_address
    
    while True:
        ip = input("Enter target IP : ")
        try:
            ip_address(ip)
            break
        except:
            print("Error. Please enter correct IP address")
    return ip

def cleanScreen():
    if sys_name == 'nt':
        system('cls')
    else:
        system('clear')
    
if __name__ == '__main__':
    try:
        banner = '''
         ___  ____   _____  ____      _      ____  _  __
        |_ _||  _ \ |_   _||  _ \    / \    / ___|| |/ /
         | | | |_) |  | |  | |_) |  / _ \  | |    | ' / 
         | | |  __/   | |  |  _ <  / ___ \ | |___ | . \ 
        |___||_|      |_|  |_| \_\/_/   \_\ \____||_|\_\\
        '''
        parser = argparse.ArgumentParser()
        parser.add_argument('-o', '--own', help='Geolocalize your own IP', action='store_true')
        parser.add_argument('-t', '--target', help='Geolocalize target IP', action='store_true')
        args = parser.parse_args()
        
        cleanScreen()
        print(RED)
        print(banner)
        print(GREEN)
        
        if args.target:
            target_ip = getTargetIP()
            print(f'Your Target IP  : {target_ip}')
            print(f'Your Target Name: {getHostName(target_ip)}')
            localiseIP(target_ip)
        elif args.own:
            host_local_ip = getHostIP()
            print(f'Your IP         : {host_local_ip}')
            print(f'Your host Name  : {getHostName(host_local_ip)}')
            localiseIP(host_local_ip)
        else:
            parser.print_help()
    except Exception as e:
        print(f'Errorr: {e}{WHITE}')
        exit(1)