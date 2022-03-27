import os
from hashlib import sha256
# import pyaudio as sp
# import os.path as path_info


# This list contain all files that we will crypt contain
all_files = list()

def open_file(path):
    """ This method permit to read file """
    with open(path, "r") as content:
        read_data = content.read()
    return read_data

def write_in_file(path, content):
    """ This method permit to read file """
    with open(path, "w+") as file:
        file.write(content)
        
    
def cesar_cipher():
    """ This function use Cesar cipher method to crypt file"""
    current_file_path = ''
    current_file_content_crypt = ''
    for i in range(len(all_files)):
        current_file_path = all_files[i]["path"] +"/"+ all_files[i]["file_name"]
        current_file_content = open_file(current_file_path)
        for i in current_file_content:
            print(ord(i))
        # current_file_content = "Make by Shadoworker5"

        # write_in_file(current_file_path, current_file_content)

def vigenere_cipher():
    """ This function use Vigenere method to crypt file """
    pass

def xor_cipher(key):
    """ This function use XOR method to crypt file """
    # current_file_path = ''
    # current_file_content_crypt = ''
    keys = sha256(key.encode('utf-8')).digest()
    for i in range(len(all_files)):
        current_file_path = all_files[i]["path"] +"/"+ all_files[i]["file_name"]
        # current_file_content = open_file(current_file_path)
        # current_file_content = "Make by Shadoworker5"
    with open('msg.txt', 'r') as f_entree:
        with open('current_file_path.txt', 'wb') as f_sortie:
            lignes = f_entree.readlines()
            if len(lignes) != 0:
                all_content = [line for line in lignes]
                cp = 0
                for item in all_content:
                    for i in range(len(item)):
                        c = ord(item[i])
                        j = cp % len(keys)
                        code = bytes([c^keys[j]])
                        # print(code)
                        f_sortie.write(code)
                        cp += 1
                    
        
        # write_in_file(current_file_path, current_file_content_crypt)
    

def search_files(path, extension):
    """ This function help you to get all files you want """
    for folder, sub_folder, files in os.walk(path):
        for item in range(len(files)):
            file_with_path = dict()
            if files[item].split(".")[1] in extension:
                file_with_path["path"] = folder
                file_with_path["file_name"] = files[item]
                all_files.append(file_with_path)


search_files("C:/Users/Kassoum/Documents/tuto/Cyber security/codes/Hacking Tools", ["txt"])
cipher_mehtods = ["Cesar", "Vigenere", "XOR"]

for key, item in enumerate(cipher_mehtods):
    print(f"[{key+1}]- {item}")

choose = int(input("Choose one: "))
if choose == 1:
    cesar_cipher();
elif choose == 2:
    vigenere_cipher()
elif choose == 3:
    xor_cipher("tartempion")
else:
    print("You choice is not found!!!!")
    exit()


# def sid2user(sid):
#     try:
#         key = OpenKey(HKEY_LOCAL_MACHINE, 'SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList'+'\\'+sid)
#         value, types = QueryValueEx(key, 'ProfileImagePath')
#         user = value.split('\\')[-1]
#         return user
#     except:
#         return sid

# def return_dir():
#     dirs = ['C:\\Recycler\\', 'C:\\Recycled\\', 'C:\\$Recycler.Bin\\']

#     for recycle in dirs:
#         if os.path.isdir(recycle):
#             print(recycle)
#             # return recycle
#     return None

# def search_file(recycle_dir):
#     dir_list = os.listdir(recycle_dir)
#     for sid in dir_list:
#         files = os.listdir(recycle_dir + sid)
#         user = sid2user(sid)
#         print(f'[*] Listing files for user {str(user)}')
#         for file in files:
#             print(f'[*] Found {str(file)}')

# def restore_file(file_name):
#     pass

# if __name__ == "__main__":
#     art.tprint("Shadoworker5")
#     recycle_dirs = return_dir()
#     # print(recycle_dirs)
#     # search_file(recycle_dirs)
#     # search_file()