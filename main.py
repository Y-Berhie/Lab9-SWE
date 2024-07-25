def main():
    while True:
        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit\n')
        option = int(input('Please enter an option: '))
        if option == 1:
            password = input('Please enter the password to encode: ')
            encoded_password = encode(password)
            print('Your password has been encoded and stored!\n')
        elif option == 2:
            print(f'The encoded password is {encoded_password}, and the original password is {decode(encoded_password)}.\n')
        elif option == 3:
            break


def encode(password):
    int_password = []
    for num in password:
        if int(num) < 7:
            int_password.append(int(num) + 3)
        elif int(num) >= 7:
            int_password.append((int(num) + 3) % 10)
    encoded_password = ""
    for i in int_password:
        encoded_password += str(i)
    return encoded_password


def decode(password):
    newstr = ""
    for num in password:
        if int(num) <= 2:
            newstr += str((int(num) - 3) + 10)
        else:
            newstr += str(int(num) - 3)
    return newstr


if __name__ == '__main__':
    main()
