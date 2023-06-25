#!/usr/bin/env python3

"""
 * @author Shadoworker5 Dev
 * @email shadoworker5@protonmail.com
 * @create date 2023-06-16 12:28:04
 * @modify date 2023-06-25 02:39:39
"""
import os
import subprocess
from requests import post as postQuery
from datetime import datetime

# To use this script you must follow this guide
## Copy this script in /etc/init.d/
## Define schedule job in crontab example */5 * * * * root /etc/init.d/services_auto_start.py
## uncomment sendNotificationToSlack or sendNotificationToDiscord about your

LOG_FILE_PATH       = "/tmp/services_auto_start.log"
SLACK_BOT_URL       = "https://hooks.slack.com/services/XXXXXXXXX/XXXXXXXXX/XXXXXXXXXXXXXXXXXX"
DISCORD_WEBHOOKS    = "https://discordapp.com/api/webhooks/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

# Define dictionnary for all service to monitor
CHECK_SERVICES  = {
    "ssh" : {
        "port"      : 22,
        "command"   : "service ssh start"
    },
    "apache2" : {
        "port"      : 80,
        "command"   : "service apache2 start"
    },
    "openvpn" : {
        "port"      : 1194,
        "command"   : "service openvpn start"
    },
    "mysql" : {
        "port"      : 3306,
        "command"   : "service mysql start"
    }
}

def executeCommande(command):
    os.system(command)

def getCurrentTime():
    return datetime.now()

def writeInLogFile(msg):
    with open(LOG_FILE_PATH, "a") as log_file:
        log_file.write(msg)
        
def checkPortStatus(port):
    result = subprocess.getoutput(f"nc -vz localhost {port}")
    writeInLogFile(f"[{getCurrentTime()}] Checking port: {port} ==> {result}\n")
    if "refused" not in result:
        return True
    else:
        return False

def checkServiceStatus():
    for i in CHECK_SERVICES:
        command = CHECK_SERVICES[i]["command"]
        if checkPortStatus(CHECK_SERVICES[i]["port"]):
            continue
        else:
            command     = CHECK_SERVICES[i]["command"]
            message     = f"[{getCurrentTime()}] Starting service {i} with command: \"{command}\" \n"
            writeInLogFile(message)
            executeCommande(command)
            # sendNotificationToSlack(message)
            # sendNotificationToDiscord(message)
            
def sendNotificationToSlack(message):
    response = postQuery(SLACK_BOT_URL, data=message)
    writeInLogFile(f"[{getCurrentTime()}] sendNotificationToSlack response: \"{response.text}\" \n")

def sendNotificationToDiscord(message):
    response = postQuery(DISCORD_WEBHOOKS, data=message)
    writeInLogFile(f"[{getCurrentTime()}] sendNotificationToDiscord response: \"{response.text}\" \n")
    
if __name__ == "__main__":
    try:
        checkServiceStatus()
    except Exception as e:
        writeInLogFile(f"Error: {str(e)}\n")