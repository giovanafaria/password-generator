import secrets
import string
import random
import pyperclip
import os
import time

characters = {
    'letters': string.ascii_letters,
    'numbers': string.digits,
    'symbols': string.punctuation,
}

def enter_password_length():
    try:
        n = int(input('\tEnter the length of your password: '))
        return n  # return the length of the password
    except ValueError:
        print('\tInvalid input. Value should be integer only.')
        print('Restarting program...')
        time.sleep(3)
        main()  # restart the program if input is invalid


def generate_password(n: int) -> str:
    password = ''
    for i in range(n):
        password += ''.join(secrets.choice(characters['letters'] + characters['numbers'] + characters['symbols']))
    return password


def main():
    os.system('clear')  # clear the terminal
    print('Startig password generator...')
    password_length = enter_password_length()
    password = generate_password(password_length)
    print('Generated password: ' + password)
    pyperclip.copy(password)
    print('Password copied to clipboard.')


if __name__ == '__main__':
    main()