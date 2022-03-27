import os, time
import art
from winreg import *
import winshell
# import sqlite3

# ATTRIB -H -R -S /S /D D:*.*
# Global variable
recyle_files_path = os.getcwd()+'\\recyle_files\\'
dirs_path = ['C:\\Recycler\\', 'C:\\Recycled\\', 'C:\\$Recycle.Bin\\']
list_menu = ['Search files', 'Show files list', 'Restore specific file', 'Restore all files', 'Exit']
delete_files_found = list()
current_usename = os.getlogin()
extension_not_restore = ['.ini']
recyle_directorie = ''

def get_user_name(id):
    try:
        key = OpenKey(HKEY_LOCAL_MACHINE, f'SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList\{id}')
        value, types = QueryValueEx(key, 'ProfileImagePath')
        return value.split('\\')[-1]
    except:
        return id

def find_directorie():
    for item in dirs_path:
        if os.path.isdir(item):
            return item
    return None

def search_file(recycle_path):
    if recycle_path:
        global recyle_directorie
        recyle_directorie = recycle_path
        all_files = os.listdir(recycle_path)
        
        for file_name in all_files:
            user = get_user_name(file_name)
            if user != current_usename:
                continue
            
            with os.scandir(recycle_path + file_name) as files:
                for i in files:
                    dict_file = dict()
                    dict_file['name'] = i.name
                    dict_file['deleted_at'] = time.ctime(os.path.getmtime(i.path))
                    delete_files_found.append(dict_file)
        print(f'{len(delete_files_found)} delete files found for user: {current_usename}')
    else:
        print(f'Error path not found')
    try_again()

def show_delte_files():
    if delete_files_found:
        print(f'{"*"*20} All delete files list {"*"*20}')
        print('*'*70)
        print('# {:<5} || {:<20} || {:<34}#'.format('ID','Filename', 'Deleted at'))
        print('*'*70)

        for key, value in enumerate(delete_files_found):
            print('# {:<5} || {:<20} || {:<34}#'.format(str(key+1), value["name"], value["deleted_at"]))
            print('*'*70)
    else:
        print(f'File list not found!!!!.\nPlease check delete files option before to show it.')
    try_again()

def restore_specific_file():
    # code
    try_again()

def restore_all_files():
    # # print()
    # filename = recyle_directorie + delete_files_found[2]
    # winshell.undelete(filename)
    try_again()

def get_input(msg, format):
    while True:
        try:
            response = format(input(msg))
            if isinstance(response, format):
                break
            else:
                print('Error type. please try again')
        except ValueError:
            print(f'Ooops!!! you must enter {format} type ')
            
    return response

def try_again():
    while True:
        response = get_input('\nDo you want to continue [Y/n] default [n]: ', str)
        if response == 'Y':
            main()
            break
        else:
            print('Good bye user')
            break

def choose_menu():
    while True:
        item = get_input('=> ', int)
        if item in range(len(list_menu) + 1):
            break
        else:
            item = get_input('=> ', int)
            print(f'Yous must choose between 1 and {len(list_menu)}')
    
    if item == 1:
        recycle = find_directorie()
        search_file(recycle)
    elif item == 2:
        show_delte_files()
    elif item == 3:
        pass
    elif item == 4:
        restore_all_files()
    else:
        print('Good bye user')
        exit()

def main():
    for i, j in enumerate(list_menu):
        print(f'[{i+1}] {j}')

    print('\nChoise  one')
    choose_menu()

if __name__ == "__main__":
    # art.tprint("Shadoworker")
    main()
    