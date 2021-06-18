import string
from secrets import randbelow

def generate(length: int, option: int) -> str:
    """Function to generate the password and output to the command line

    Parameters
    ----------
    length : int, required
        The length of password to be generated
    option : int, required
        Type of password to be generated
            1 - alphabetic lowercase
            2 - alphabetic mixed
            3 - alphanumeric
            4 - alphanumeric + special characters

    Returns
    -------
    password : str
        Randomly generated password
    """

    special_characters = '~`!@#$%^&*-_+=/?.' # special character list
    password = ''

    # building the charpool
    if option >= 1:
        charpool = string.ascii_lowercase
    if option >= 2:
        charpool = charpool + string.ascii_uppercase
    if option >= 3:
        charpool = charpool + string.digits
    if option == 4:
        charpool = charpool + string.punctuation

    charpool_length = len(charpool)

    # generating random password
    for _ in range(length):
        password = f'{password}{charpool[randbelow(charpool_length)]}'
    return password
