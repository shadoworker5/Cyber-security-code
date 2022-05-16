"""
 * @author Kassoum TRAORE
 * @email shadoworker5.dev@gmail.com
 * @create date 2022-05-15 23:37:46
 * @modify date 2022-05-16 00:09:57
 * @desc [description]
"""
import os
import json
import base64
import win32crypt
from Crypto.Cipher import AES
from datetime import datetime, timedelta
import sqlite3

menu_list = [
    'Brave history', 'Password save in Brave',
    'Chrome history','Password save in Chrome',
    'Firefox history', 'Password save in Firefox',
    'Microsoft Edge history', 'Password save in Microsoft Edge',
    'Clean history', 'Clean password',
    'Exit'
]

database_path = {
    'brave_history'     : f'{os.environ["USERPROFILE"]}/AppData/Local/BraveSoftware/Brave-Browser/User Data/Default/History',
    'brave_login_data'  : f'{os.environ["USERPROFILE"]}/AppData/Local/BraveSoftware/Brave-Browser/User Data/Default/Login Data',
    'chrome_history'    : f'{os.environ["USERPROFILE"]}/AppData/Local/Google/Chrome/User Data/Default/History',
    'chrome_login_data' : f'{os.environ["USERPROFILE"]}/AppData/Local/Google/Chrome/User Data/Default/Login Data'
}

local_state_path = {
    'brave'  : f'{os.environ["USERPROFILE"]}/AppData/Local/BraveSoftware/Brave-Browser/User Data/Local State',
    'chrome' : f'{os.environ["USERPROFILE"]}/AppData/Local/Google/Chrome/User Data/Local State'
}

def choose_yes_no(msg):
    while True:
        try:
            choose = str(input(f"{msg} [y/n] default[n]: "))
            if choose.upper() == 'Y' or choose.upper() == 'N':
                break
            if len(choose) == 0:
                choose = 'n'
                break
        except ValueError:
            print("Please choose between Y or N")
            continue
    return choose.upper()

def save_in_file(message):
    response = choose_yes_no('\nDo you want to save your message?')

    if response == 'Y':
        file_name = str(datetime.timestamp(datetime.today())).split('.')[0]+'.txt'
        
        with open(file_name, 'w') as file:
            file.write(message)
        print('Message successfully\n')
    main()

def db_connection(database):
    sqlite_db = sqlite3.connect(database)
    return sqlite_db.cursor()

def chrome_date_and_time(chrome_data):
    if chrome_data:
        return datetime(1601, 1, 1) + timedelta(microseconds=chrome_data)
    else:
        return 0

def get_encryption_key(browser):
    local_computer_directory_path = local_state_path[browser]

    with open(local_computer_directory_path, "r", encoding="utf-8") as f:
        local_state_data = f.read()
        local_state_data = json.loads(local_state_data)

    encryption_key = base64.b64decode(local_state_data["os_crypt"]["encrypted_key"])[5:]
    
    return win32crypt.CryptUnprotectData(encryption_key, None, None, None, 0)[1]

def decode_password(password, encryption_key):
    try:
        iv = password[3:15]
        password = password[15:]
        cipher = AES.new(encryption_key, AES.MODE_GCM, iv)
        return cipher.decrypt(password)[:-16].decode()
    except:
        try:
            return str(win32crypt.CryptUnprotectData(password, None, None, None, 0)[1])
        except:
            return "No Passwords"

def browser_history(browser):
    db_query = db_connection(database_path[browser+'_history'])
    history = db_query.execute('SELECT title, url, visit_count, last_visit_time FROM urls').fetchall()
    print(f'+{"-"*100}+')
    print(f'| {" ":<35} List of history ({len(history)}) {" ":<41} |')
    print(f'+{"-"*100}+')

    for item in history:
        print(f'| Title : {item[0]}')
        print(f'| Url   : {item[1]}')
        print(f'| Visit count: {item[2]}')
        print(f'| Last time visit: {chrome_date_and_time(item[3])}')
        print(f'|{"-"*100}|')
    # save_in_file(base64.encode(history))
    print('\n')
    main()

def browser_password(browser):
    db_query = db_connection(database_path['chrome_login_data'])
    user_password = db_query.execute('SELECT origin_url, action_url, username_value, password_value, federation_url, date_created, times_used, date_last_used, date_password_modified FROM logins').fetchall()
    print(f'+{"-"*100}+')
    print(f'| {" ":<35} List of user_password ({len(user_password)}) {" ":<35} |')
    print(f'+{"-"*100}+')
    encryption_key = get_encryption_key(browser)
    
    for item in user_password:
        print(f'| Origin url : {item[0]}')
        print(f'| Action url   : {item[1]}')
        print(f'| Username value : {item[2]}')
        print(f'| Password value : {decode_password(item[3], encryption_key)}')
        print(f'| Federation url : {item[4]}')
        print(f'| Created at : {chrome_date_and_time(item[5])}')
        print(f'| Time used : {item[6]}')
        print(f'| Date last time use : {chrome_date_and_time(item[7])}')
        print(f'| Date password modified : {chrome_date_and_time(item[8])}')
        print(f'|{"-"*100}|')
    # save_in_file(user_password)
    print('\n')
    main()

def clean_browser_history(browser=''):
    pass

def clean_browser_password(browser=''):
    pass

def get_input(msg, format):
    while True:
        try:
            response = format(input(msg))
            if isinstance(response, format):
                break
            else:
                print('Error. Please try agina')
        except ValueError:
            print(f'Ooops!!! you must enter data of {format} type')
    return response

def choose_menu(list_menu):
    while True:
        item = get_input('#> ', int)
        if item in range(1, len(list_menu) + 1):
            break
        else:
            item = get_input('#> ', int)
            print(f'Vous devez choisir entre 1 et {len(list_menu)}')
    
    if item == 1:
        browser_history('brave')
    elif item == 2:
        browser_password('brave')
    elif item == 3:
        browser_history('chrome')
    elif item == 4:
        browser_password('chrome')
    elif item == 5:
        print('In progress.................')
        exit()
    elif item == 6:
        print('In progress.................')
        exit()
    elif item == 7:
        print('In progress.................')
        exit()
    elif item == 8:
        print('In progress.................')
        exit()
    elif item == 9:
        print('In progress.................')
        exit()
    elif item == 10:
        print('In progress.................')
        exit()
    else:
        print('Good bye....................')
        exit()

def main():
    for i, value in enumerate(menu_list):
        print(f'[{str(i+1)}]- {value}')
    print('\nChoose one')
    choose_menu(menu_list)

if __name__ == '__main__':
    main()