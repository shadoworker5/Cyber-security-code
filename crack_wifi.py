import subprocess
import re

list_wifi = list()

def crack_wifi_key(name, host_ip):
    pass

def get_wifi_user(host_ip):
    pass

def scan_wifi():
    print("Loading...............")
    result = subprocess.check_output(["netsh", "wlan", "show", "network", "mode=Bssid"], shell=True, text=True)
    if re.findall("Actuellement 0", result):
        print("No Wi-Fi detected ")
    else:
        convert_scan_data = re.findall(".*SSID.*", result)
        for i in range(0, len(convert_scan_data), 2):
            dict_wifi = dict()
            dict_wifi['SSID'] = convert_scan_data[i].split("ÿ:")[1][1::]
            dict_wifi['BSSID'] = convert_scan_data[i+1].split("ÿ:")[1][1::]
            list_wifi.append(dict_wifi)
        print(list_wifi)

def get_input():
    result = 0
    while True:
        try:
            response = int(input("##> "))
        except:
            print("You must input only integer value")
            continue

        if response in range(1, 4):
            result = response
            break
        else:
            print("Please choose between 1 and 3")
    return result

def main():
    art.tprint("Shadoworker5")
    print("Choose 1 option")
    print('[1] Scan WI-FI available')
    print('[2] Crack WI-FI key ')
    print('[3] Exit')
    choose = get_input()
    if choose == 1:
        scan_wifi()
    elif choose == 2:
        print('Module not found')
        exit()
    elif choose == 3:
        exit()

if __name__ == '__main__':
    main()