import json

all_social_name = ['facebook.com', 'twitter.com', 'instagram.com', 'tiktok.com']
all_social_number = ['wa.me', 't.me', 'tiktok.com']
all_menus = ['Name', 'Pseudo', 'E-mail', 'Phone number', 'Country', 'Photo', 'PIN', 'IP address']

def search_by_name():
    print('Enter username to search')
    name = get_input('=> ', str)
    url = ''
    for item in all_social_name:
        url = f'wwww.{item}/{name}'
        print(url)
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
        response = get_input('Do you want to try again [Y/n] default [n]: ', str)
        if response == 'Y':
            main()
            break
        else:
            print('Good bye user')
            break

def choose_menu():
    while True:
        item = get_input('=> ', int)
        if item in range(len(all_menus) + 1):
            break
        else:
            item = get_input('=> ', int)
            print(f'Yous must choose between 1 and {len(all_menus)}')
    
    if item == 1:
        search_by_name()

def main():
    for i, j in enumerate(all_menus):
        print(f'[{i+1}] {j}')

    print('\nChoise your tool')
    choose_menu()

if __name__ == '__main__':
    # tprint('Shadoworker5 Search Tools')
    # main()
    api_key = json('api/key')
    print(api_key)
