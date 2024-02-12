import secrets
import string
import pyperclip
import os
import time

characters = {
    'letters': string.ascii_letters,
    'numbers': string.digits,
    'symbols': string.punctuation,
}


def enter_password_length():
    """
    This function prompts the user to enter the length of the password they would like to generate.
    It returns the length of the password as an integer.

    Args:
        None

    Returns:
        int: The length of the password as an integer

    Raises:
        ValueError: If the input is not a valid integer
    """
    while True:
        try:
            n = int(input('\tEnter the length of your password: '))
            return n  # return the length of the password
        except ValueError:
            print('\tInvalid input. Value should be integer only.')
            print('Restarting program...')
            time.sleep(3)


def generate_password(n: int) -> str:
    """ 
    Generate a random password of length n.

    Args:
        n (int): The length of the password to generate.

    Returns:
        str: The generated password.
    """ 
    password = ''
    for i in range(n):  # generates the password randomly with the range specified
        password += ''.join(secrets.choice(characters['letters'] +
                                           characters['numbers'] +
                                           characters['symbols']))
    return password


def main():
    os.system('clear')  # clear the terminal
    print('Startig password generator...')
    while True: 
        password_length = enter_password_length()
        if password_length > 0:  # check if input if valid
            break
    password = generate_password(password_length)
    print('Generated password: ' + password)
    pyperclip.copy(password)  # coping password to clipboard
    print('Password copied to clipboard.')


if __name__ == '__main__':
    main()
