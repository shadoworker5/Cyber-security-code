"""
 * @author Kassoum TRAORE
 * @email shadoworker5.dev@gmail.com
 * @create date 2021-11-27 18:48:48
 * @modify date 2022-04-18 00:53:28
 * @desc [description]
"""
import math
from random import randint, randrange
from string import printable
from secrets import randbelow

import numpy
# import art

list_of_key = {}
ALL_CHAR = [i for i in printable if ord(i) > 13]
ALPHABET_SIZE = len(ALL_CHAR)
menu_list = [
    'Affine crypt', 'Affine decrypt', 'Ceasar crypt', 'Ceasar decrypt', 'El Gamal crypt', 'El Gamal decrypt', 'Hill crypt', 'Hill decrypt', 'RSA crypt', 'RSA decrypt', 'Vigenere crypt', 'Vigenere decrypt', 'Load in file', 'Exit'
]

def generate_random_value(m):
    while True:
        d = randbelow(1000000)
        if pgcd(d, m) == 1:
            break     
    return d

def generate_random_prime_value(m=1000000):
    while True:
        d = randbelow(m)
        if d % 2 != 0:
            break
    return d

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

def choose_yes_no(msg):
    choose = 'N'
    while True:
        try:
            choose = str(input(f"{msg} [Y/N] default[N]: ")).upper()
            if choose == 'Y' or choose == 'N':
                break
        except ValueError:
            print("Please choose between Y or N")
            continue
    return choose

def save_in_file(message):
    response = choose_yes_no('\nDo you want to save your message?')

    if response == 'Y':
        from datetime import datetime
        
        file_name = str(datetime.timestamp(datetime.today())).split('.')[0]+'.txt'
        
        with open(file_name, 'w') as file:
            file.write(message)
        print('Message successfully\n')
    main()

def create_message(msg):
    while True:
        message = input(msg)
        if message != '':
            break
    return message

def key_decrypt(key):
    if key % 2 == 0:
        return key
    else:
        return pow(key, -1, ALPHABET_SIZE)

def pgcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def affine_ceasar_encrypt(char, a, b):
    """
    This is use to encrypt char
    Formula: E(x) = (a*x + b) mod(ALPHABET_SIZE)
    """
    E = (a * ALL_CHAR.index(char) + b) % ALPHABET_SIZE
    return ALL_CHAR[E]

def affine_ceasar_decrypt(char, a, b):
    """
    This is use to encrypt char
    Formula: D(x) = a^-1 * (x - b) mod(ALPHABET_SIZE)
    """
    D = (key_decrypt(a) * (ALL_CHAR.index(char) - b)) % ALPHABET_SIZE
    return ALL_CHAR[D]

def affine_crypt():
    print('Encode format: E(x) = (a*x + b) mod(size)')
    encode_msg = ""
    plain_text = create_message('Enter your message: ')
    a = int(get_prime_number('Enter value of a: '))
    b = int(input('Enter value of b: '))
    print(f"\nPlain message: {plain_text}")

    for i in plain_text:
        encode_msg += affine_ceasar_encrypt(i, a, b)
    print(f'\nCipher message: {encode_msg}')
    save_in_file(encode_msg)

def affine_decrypt():
    print('Decode format: D(x) = a^-1 * (x - b) mod(ALPHABET_SIZE)')
    decode_msg = ""
    cipher_text = create_message('Enter your message: ')
    a = int(get_prime_number('Enter value of a: '))
    b = int(input('Enter value of b: '))
    print(f'Cipher message: {cipher_text}')

    for i in cipher_text:
        decode_msg += affine_ceasar_decrypt(i, a, b)
    
    print(f'Plain message: {decode_msg}')
    save_in_file(decode_msg)

def ceasar_crypt():
    print('\nEncode format: E(x) = (x + b) mod(size)')
    plain_text = create_message('Enter your message: ')
    b = int(input('Enter value of b: '))
    print(f'\nPlain message: {plain_text}')
    encode_msg = ""
    
    for i in plain_text:
        encode_msg += affine_ceasar_encrypt(i, 1, b)
    
    print(f'\nCipher message: {encode_msg}')
    save_in_file(encode_msg)

def ceasar_decrypt():
    print('Decode format: D(x) = (x - b) mod(ALPHABET_SIZE)')
    cipher_text = create_message('Enter your message: ')
    b = int(input('Enter value of b: '))
    encode_msg = ""
    print(f'Cipher message: {cipher_text}')
    
    for i in cipher_text:
        encode_msg += affine_ceasar_decrypt(i, 1, b)
    print(f'Plain message: {encode_msg}')
    save_in_file(encode_msg)

def generate_random_prime_el_gamal():
    while True:
        n = randrange(pow(20, 30), pow(15, 50))
        if n % 2 != 0:
            break
    return n
    
def generate_random_el_gamal(p):
    while True:
        value = randrange(0, p)
        if pgcd(value, p) == 1 and value & 1 == 1:
            break
    return value

# Modular exponentiation
def exponentiation(a, b, n):
    # if b % 2 == 1: result = (result * a) % n a = (a * a) % n b //= 2
    result = 1
    while b > 0:
        if b & 1 == 1: # b%2==1
            result = (result * a) % n
        a = (a*a) % n
        b = b >> 1 # b /=2
        
    return result

def el_gamal_crypt():
    # plain_text = create_message("Enter your message: ")
    p = generate_random_prime_el_gamal()
    a = generate_random_el_gamal(p - 2)
    m = generate_random_el_gamal(p - 1)
    n = exponentiation(m, a, p)
    k = generate_random_el_gamal(p - 1)
    print(f'Public key (p, m, n): \np: {p}\nm: {m}\nn: {n}')
    print(f'\nPrivate key a:\na: {a}')
    
    cipher_txt = ''
    plain_text = 'Encryption is science of secret'
    y1 = exponentiation(m, k, p)
    coef = exponentiation(n, k, p)
    for i in plain_text:
        cipher_txt += str(ALL_CHAR.index(i) * coef) + ' '
        
    print(f'Cipher message: {cipher_txt}\n')
    el_gamal_decrypt(cipher_txt, y1, p, a)

def el_gamal_decrypt(msg, y1, p, a):
    msg = [int(i) for i in msg.split()]
    decode_txt = ''
    coef = exponentiation(y1, a, p)
    
    for i in msg:
        key = int(i / coef)
        decode_txt += ALL_CHAR[key]
    
    print(f'Plain messages: {decode_txt}')

def hill_crypt():
    print(""" (x1, x2) global form """)
    print(""" Key = (a, b, c, d) """)
    print(""" PGCD(ad-bc, 26)=1 """)
    print(""" y1= (ax1 + bx2)mod26 and y2= (cx1 + dx2)mod26 with 0 =< y =< 25 """)
    print(ALL_CHAR)
    
def hill_decrypt():
    print(""" (x1, x2) global form """)
    print(""" Key = (a, b, c, d) """)
    print(""" PGCD(ad-bc, 26)=1 """)
    print(""" x1= (ad-bc)^-1(dy1 - by2)mod26 and x2= (ad-bc)^-1(-cy1 + ay2)mod26 with 0 =< x =< 25 """)
    
def CalculerClesRsa(p, q):
    n=p*q 
    m=(p-1)*(q-1)
    d = generate_random_value(m)
    c = pow(d, -1, m)
    list_of_key['c'] = d
    list_of_key['n'] = n
    list_of_key['d'] = c
    print(f"Public key: (c: {c}, n: {n}) \nPrivate key: (d: {d}, n: {n})\n")

def get_prime_number(msg):
    while True:
        try:
            response = int(input(msg))
            if isinstance(response, int):
                if response % 2 != 0:
                    break
                else:
                    print("Please choose prime number")
            else:
                print('Erreur. Please choose integer value')
        except ValueError:
            print(f'Ooops!!! you must enter data of {int} type')
    return response

def get_rsa_key_value():
    p = get_prime_number('Please choose enter value of p: ')
    q = get_prime_number('Please choose enter value of q: ')
    while True:
        if p == q:
            print("Please choose different value for p and q")
            p = get_prime_number('Please choose  enter value of p: ')
            q = get_prime_number('Please choose  enter value of q: ')
        else:
            break
    CalculerClesRsa(p, q)

def get_public_private_key(i):
    if i in list_of_key.keys():
        i = list_of_key[i]
        n = list_of_key['n']
    else:
        i = get_prime_number(f'Please choose  enter value of {i}: ')
        n = get_prime_number('Please choose  enter value of n: ')
    return i, n

def rsa_crypt():
    print("Public key format: (c, n)\n")

    calculate_key = choose_yes_no("Do you want to calculate your cipher key?")
    if calculate_key == 'Y':
        get_rsa_key_value()
    
    c, n = get_public_private_key('c')
    encode_msg = ""
    plain_text = get_input("Enter you message: ", str)
    print(f"\nPlain message: {plain_text} \n")

    for i in plain_text:
        y = pow(ALL_CHAR.index(i), c) % n
        encode_msg += str(y) + ' '
        
    print(f"Cipher message: {encode_msg}")
    save_in_file(encode_msg)

def rsa_decrypt():
    print("Private key format: (d, n)\nMessage format: 11 222 33 44\n")

    calculate_key = choose_yes_no("Do you want to calculate your cipher key?")
    if calculate_key == 'Y':
        get_rsa_key_value()
    
    d, n = get_public_private_key('d')
    decode_msg = ""
    cipher_message = get_input("Enter you message: ", str)
    print(f"\nCipher message: {cipher_message} \n")

    try:
        cipher_message = [int(i) for i in cipher_message.split()]
    except Exception:
        print("Message is incorrect.\nPlease try again")
        main()
    
    for i in cipher_message:
        x = pow(i, d) % n
        decode_msg += ALL_CHAR[x]
    print(f"\nPlain message: {decode_msg}")
    save_in_file(decode_msg)

def vigenere_crypt():
    plan_text = create_message('Enter your message: ')
    key = create_message('Enter your key text: ')
    encode_msg = ""
    key_generate = (key*len(plan_text))[0:len(plan_text)]
    print(f'\nPlain message: {plan_text}')
    
    for i in range(len(plan_text)):
        char_code = (ALL_CHAR.index(plan_text[i]) + ALL_CHAR.index(key_generate[i])) % len(ALL_CHAR)
        encode_msg += ALL_CHAR[char_code]
        
    print(f'\nCipher message: {encode_msg}')
    save_in_file(encode_msg)

def vigenere_decrypt():
    plan_text = create_message('Enter your message: ')
    key = create_message('Enter your key text: ')
    decode_msg = ""
    key_generate = (key*len(plan_text))[0:len(plan_text)]
    print(f'\nCipher message: {plan_text}')

    for i in range(len(plan_text)):
        char_decode = ALL_CHAR.index(plan_text[i]) - ALL_CHAR.index(key_generate[i])
        decode_msg += ALL_CHAR[char_decode]
        
    print(f'Plain message: {decode_msg}')
    save_in_file(decode_msg)

def choose_menu(list_menu):
    while True:
        item = get_input('#> ', int)
        if item in range(1, len(list_menu) + 1):
            break
        else:
            item = get_input('#> ', int)
            print(f'Vous devez choisir entre 1 et {len(list_menu)}')
    
    if item == 1:
        affine_crypt()
    elif item == 2:
        affine_decrypt()
    elif item == 3:
        ceasar_crypt()
    elif item == 4:
        ceasar_crypt()
    elif item == 5:
        el_gamal_crypt()
    elif item == 6:
        el_gamal_decrypt()
    elif item == 7:
        # hill_crypt()
        print('In progress.................')
    elif item == 8:
        # hill_decrypt()
        print('In progress.................')
    elif item == 9:
        rsa_crypt()
    elif item == 10:
        rsa_decrypt()
    elif item == 11:
        vigenere_crypt()
    elif item == 12:
        vigenere_decrypt()
    elif item == 13:
        print('In progresse.................')
    else:
        print('Good bye..................')
        exit()

def main():
    for i, value in enumerate(menu_list):
        print('[{}]-{}'.format(str(i+1), value))
    print('\nChoose one')
    choose_menu(menu_list)

if __name__ == "__main__":
    el_gamal_crypt()
    # art.tprint("Shadoworker5")
    # try:
    #     main()
    # except KeyboardInterrupt:
    #     print('Keyboadr interruption.\nGood bye!!!')
    #     exit()