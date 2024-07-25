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
