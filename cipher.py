import string
from secrets import randbelow
import art

ALL_CHAR = [i for i in string.printable if ord(i) > 13]
ALPHABET_SIZE = len(ALL_CHAR)
list_des_clefs = {}

def drap_chart(datas):
    import matplotlib.pyplot as py_chart
    import numpy as np
    
    char_count = list()
    char_label = list()

    for data in datas:
        for key, value in data.items():
            char_label.append(key)
            char_count.append(value)
    
    py_chart.pie(np.array(char_count), labels=char_label, shadow=True)
    py_chart.show()

def analyse_ic(dataset):
    result = 0.0
    ALPHABET_SIZE_count = 0.0

    for data in dataset:
        for i in data.values():
            result += i* (i-1)
            ALPHABET_SIZE_count += i
    if ALPHABET_SIZE_count == 0.0:
        print(0.0)
    else:
        print(result / (ALPHABET_SIZE_count * (ALPHABET_SIZE_count-1)))
            
def crack_vigener(message) -> str:
    pass

def save_in_file(message):
    from datetime import datetime
    file_name = str(datetime.timestamp()).split('.')[0]
    with open(file_name+'.txt', 'w') as file:
        file.write(message)
    print('Message save with success')

def create_message(msg):
    message = ''
    while True:
        message = input(msg)
        if message != '':
            break
    return message.upper()

def frequency_analyse(message):
    all_char = [i for i in message]
    set_char = set(all_char)
    all_char_count = list()

    for i in set_char:
        dict_char = dict()
        if i == " ":
            dict_char['space'] = all_char.count(i)
            all_char_count.append(dict_char)
            continue
        dict_char[i] = all_char.count(i)
        all_char_count.append(dict_char)
    analyse_ic(all_char_count)

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
    plan_text = create_message('Enter your message: ')
    a = int(input('Enter value of a: '))
    b = int(input('Enter value of b: '))
    print(plan_text)

    for i in plan_text:
        if i == " ":
            encode_msg += " "
            continue
        encode_msg += affine_ceasar_encrypt(i, a, b)
    print(encode_msg)

def affine_decrypt():
    print('Decode format: D(x) = a^-1 * (x - b) mod(ALPHABET_SIZE)')
    decode_msg = ""
    cipher_text = create_message('Enter your message: ')
    a = int(input('Enter value of a: '))
    b = int(input('Enter value of b: '))
    print(cipher_text)

    for i in cipher_text:
        if i == " ":
            decode_msg += " "
            continue
        decode_msg += affine_ceasar_decrypt(i, a, b)
    
    print(decode_msg)

def ceasar_crypt():
    print('Encode format: E(x) = (x + b) mod(size)')
    plan_text = create_message('Enter your message: ')
    b = int(input('Enter value of b: '))
    encode_msg = ""
    for i in plan_text:
        if i == " ":
            encode_msg += " "
            continue
        encode_msg += affine_ceasar_encrypt(i, 1, b)
    print(encode_msg)

def ceasar_decrypt():
    print('Decode format: D(x) = (x - b) mod(ALPHABET_SIZE)')
    cipher_text = create_message('Enter your message: ')
    b = int(input('Enter value of b: '))
    encode_msg = ""
    for i in cipher_text:
        if i == " ":
            encode_msg += " "
            continue
        encode_msg += affine_ceasar_decrypt(i, 1, b)
    print(encode_msg)

def vigenere_encrypt():
    plan_text = create_message('Enter your message: ')
    key = create_message('Enter your key text: ')
    encode_msg = ""
    key_generate = (key*len(plan_text))[0:len(plan_text)]
    
    for i in range(len(plan_text)):
        if plan_text[i] == " ":
            encode_msg += " "
            continue
        char_code = ALL_CHAR.index(plan_text[i]) + ALL_CHAR.index(key_generate[i])
        if char_code >= 26:
            char_code -= 26
        encode_msg += ALL_CHAR[char_code]
    print(encode_msg)

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


def generate_d(m):
    while True:
        d = randbelow(10000)
        if pgcd(d, m) == 1:
            break
    return d
    
def CalculerClesRsa(p, q):
    n=p*q 
    m=(p-1)*(q-1)
    d = generate_d(m)
    c = pow(d, -1, m)
    list_des_clefs['c'] = d
    list_des_clefs['n'] = n
    list_des_clefs['d'] = c
    print(f"\n(c: {c}, n: {n}, d: {d})")
    print(f"Clé publique: (c: {c}, n: {n}) \nClé privé: (d: {d})\n")
    # main()

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

def get_key_value():
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

def rsa_crypt():
    get_key_value()
    # print(f"\nMessage en clair: {txtClair} \n")
    
    # for i in txtClair:
    #     if i == " ":
    #         encode_msg += "500"
    #         continue
    #     y = pow(ALL_CHAR.index(i), c) % n
    #     encode_msg += str(y) + ' '
        
    # print(f"Message chiffré: {encode_msg}")
    # # sauvegarder(encode_msg)
    

def rsa_decrypt():
    pass
    # decode_msg = ""
    # print(f"\nMessage en chiffré: {txtChiffre}\n")
    # try:
    #     ciphet_text = [int(i) for i in txtChiffre.split()]
    # except Exception:
    #     print("Le format du message est incorrect.\nVeuillez reessayer svp!!!!")
    #     main()
    
    # for i in ciphet_text:
    #     if i == "500":
    #         decode_msg += " "
    #         continue
    #     x = pow(i, d) % list_des_clefs['n']
    #     decode_msg += ALL_CHAR[x]
        
    # print(f"Message en clair: {decode_msg}")
    # sauvegarder(decode_msg)
    # main()

def el_gamal_crypt():
    pass

def el_gamal_decrypt():
    pass

def vigenere_decrypt():
    plan_text = create_message('Enter your message: ')
    key = create_message('Enter your key text: ')
    decode_msg = ""
    key_generate = (key*len(plan_text))[0:len(plan_text)]

    for i in range(len(plan_text)):
        if plan_text[i] == " ":
            decode_msg += " "
            continue
        char_decode = ALL_CHAR.index(plan_text[i]) - ALL_CHAR.index(key_generate[i])
        decode_msg += ALL_CHAR[char_decode]
    print(decode_msg)

def prime_number_of_ALPHABET_SIZE_size(ALPHABET_SIZE_size):
    prime_list = list()
    for i in range(ALPHABET_SIZE_size):
        if i % 2 != 0 and i < 25:
            prime_list.append(i)    
    return prime_list

def brute_force_affine():
    cipher_text = create_message('Enter your message: ')
    print("Decrypt start......................")
    prime_list = prime_number_of_ALPHABET_SIZE_size(len(ALL_CHAR))
    decode_list = list()

    for i in prime_list:
        for j in range(0, 26):
            result = affine_decrypt(cipher_text, i, j)
            decode_list.append(result)

    with open('brute_force_affine2.txt', 'w') as file:
        for item in decode_list:
            file.write(item+"\n")
    print("Decrypt end......................")

def brute_force_ceasar():
    cipher_text = create_message('Enter your message: ')
    print("Decrypt start......................")
    # time_start = datetime.timestamp(datetime.today())
    decode_list = list()

    for j in range(0, 26):
        result = ceasar_decrypt(cipher_text, j)
        decode_list.append(result)

    with open('brute_force_ceasar2.txt', 'w') as file:
        for item in decode_list:
            file.write(item+"\n")
    print("Decrypt end......................")
    # end_start = datetime.timestamp(datetime.today())
    # print("Scan time: {} seconds".format(str(end_start - time_start)))

# def get_input(menu):
#     result = 0
#     while True:
#         try:
#             response = int(input("#> "))
#         except:
#             print("You must input only integer value")
#             continue

#         if response in range(1, len(menu)+1):
#             result = response
#             break
#         else:
#             print("Please choose between 1 and {}".format(len(menu)))
#     return result

def get_input(msg, format):
    while True:
        try:
            response = format(input(msg))
            if isinstance(response, format):
                break
            else:
                print('Erreur. Veuillez réessayer svp')
        except ValueError:
            print(f'Ooops!!! vous devez saisir une donné de type {format}')
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
        # get_key_value()
        ...
    elif item == 2:
        # create_message('ChiffrerRsa')
        ...
    elif item == 3:
        # create_message('DechiffrerRsa')
        ...
    else:
        print('Au revoir')
        exit()

def main():
    menu_list = [
        'Affine crypt', 'Affine decrypt', 'Ceasar crypt', 'Ceasar decrypt', 'Hill crypt', 'Hill decrypt', 'Vigenere encrypt',
        'Vigenere decrypt', 'RSA crypt', 'RSA derypt', 'Brute force affine', 'Brute force ceasar', 'Exit'
    ]
    for i, value in enumerate(menu_list):
        print('[{}]-{}'.format(str(i+1), value))
    print('\nChoose one')
    choose_menu(menu_list)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('Interruption touche clavier.\nAu revoir!!')
        exit()

    # hill_crypt()

    # art.tprint("Shadoworker5")
    # print("Choose 1 option")


    # choose = get_input(menu_list)
    # if choose == 1:
    #     affine_crypt()
    # elif choose == 2:
    #     affine_decrypt()
    # elif choose == 3:
    #     ceasar_crypt()
    # elif choose == 4:
    #     ceasar_decrypt()
    # elif choose == 5:
    #     vigenere_encrypt()
    # elif choose == 6:
    #     vigenere_decrypt()
    # elif choose == 7:
    #     brute_force_affine()
    # elif choose == 8:
    #     brute_force_ceasar()
    # else:
    #     exit()
