def main():
    while True:
        print('Menu')
        print('_____________')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit\n')
        option = int(input('Please enter an option: '))
        if option == 1:
            password = input('Please enter the password to encode: ')
            print('Your password has been encoded and stored!\n')
        elif option == 2:
            print(f'The encoded password is {encode(password)}, and the original password is {password}.\n')
        elif option == 3:
            break


def encode(password):
    list_password = []
    for i in password:
        list_password.append(int(i))
    updated_list = [num + 3 for num in list_password]
    final_list = []
    for i in updated_list:
        final_list.append(str(i))
    return final_list


def decode(password):
    pass
