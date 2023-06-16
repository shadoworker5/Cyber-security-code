#!/usr/bin/env python3

"""
 * @author Shadoworker5 Dev
 * @email shadoworker5@protonmail.com
 * @create date 2023-06-16 12:28:04
 * @modify date 2023-06-16 15:10:32
"""
import os
import subprocess

# You need to define schedule job in crontab after copy this script in /etc/init.d/
# */5 * * * * root /etc/init.d/services_auto_start.py > /tmp/services_auto_start.log

# Define here all TCP port, services and commands
TCP_PORTS       = ["80", "443", "3306"]
TCP_COMMANDS    = ["service apache2 start", "service mysql start"]
TCP_SERVICES    = ["apache2", "mysql"]

# Define here all UDP port, services and commands
UDP_PORTS       = ["1194"]
UDP_COMMANDS    = ["service openvpn start"]
UDP_SERVICES    = ["openvpn"]

def startService(command):
    try:
        os.system(command)
    except Exception as e:
        print(f"Error when execute {command} exception: {str(e)}")
        
def checkPortStatus(port):
    result = subprocess.check_output(f"nc -vz localhost {port} | grep refused", shell=True)
    print(f"checking port: {port} ==> {result}")
    if "refused" not in result:
        return True
    else:
        return False

def loadTcpService():
    for i in range(len(TCP_PORTS)):
        command = TCP_COMMANDS[i]
        if checkPortStatus(TCP_PORTS[i]):
            continue
        else:
            print(f"starting service: {TCP_SERVICES[i]} with command: {command}")
            startService(command)

def loadUdpService():
    for i in range(len(UDP_PORTS)):
        command = UDP_COMMANDS[i]
        if checkPortStatus(UDP_PORTS[i]):
            continue
        else:
            print(f"starting service: {TCP_SERVICES[i]} with command: {command}")
            startService(command)

def sendNotificationSlack(message):
    ...
    
if __name__ == '__main__':
    loadTcpService()
    loadUdpService()