import string

ALL_CHAR = [i for i in string.printable if ord(i) > 13]
ALPHABET_SIZE = len(ALL_CHAR)

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

def prime_number_of_ALPHABET_SIZE_size(ALPHABET_SIZE_size):
    prime_list = list()
    for i in range(ALPHABET_SIZE_size):
        if i % 2 != 0 and i < 25:
            prime_list.append(i)
    return prime_list

def crack_vigener(message) -> str:
    pass

def create_message(msg):
    message = ''
    while True:
        message = input(msg)
        if message != '':
            break
    return message.upper()

def key_decrypt(key):
    if key % 2 == 0:
        return key
    else:
        return pow(key, -1, ALPHABET_SIZE)

def affine_ceasar_decrypt(char, a, b):
    """
    This is use to encrypt char
    Formula: D(x) = a^-1 * (x - b) mod(ALPHABET_SIZE)
    """
    D = (key_decrypt(a) * (ALL_CHAR.index(char) - b)) % ALPHABET_SIZE
    return ALL_CHAR[D]

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