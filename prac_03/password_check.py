MINIMUM_LENGTH = 4


#refactor password check program to use functions


def main():
    password = get_password()
    while len(password) < MINIMUM_LENGTH:
        password = get_password()

    asterisks(password)


def asterisks(password):
    print('*' * len(password))


def get_password():
    password = input("Enter password of at least {} characters: ".format(MINIMUM_LENGTH))
    return password


main()

