"""  encryption_fun purpose it to encrypt or decrypt a user imputed message. """

import string # Allows for use of Strings library
import random# Allows for use of random python library

""" Begin id_generator which will return a random two character
    string of capital letters, lower case letters, or 0-9 digits. """
def id_generator(size=2, char=string.ascii_letters + string.digits):
    return ''.join(random.choice(char) for _ in range(size))
# End id_generator

print(id_generator())# Test to see if id_generator is working.

""" The lib dictionary holds all accepted characters which every execution of the program will call
id_generator and assign a new conversion to each character. """
lib = {'a': id_generator(), 'b': id_generator(), 'c': id_generator(), 'd': id_generator(), 'e': id_generator(),
       'f': id_generator(), 'g': id_generator(), 'h': id_generator(), 'i': id_generator(), 'j': id_generator(),
       'k': id_generator(), 'l': id_generator(), 'm': id_generator(), 'n': id_generator(), 'o': id_generator(),
       'p': id_generator(), 'q': id_generator(), 'r': id_generator(), 's': id_generator(), 't': id_generator(),
       'u': id_generator(), 'v': id_generator(), 'w': id_generator(), 'y': id_generator(), 'x': id_generator(),
       'z': id_generator(), ' ': id_generator()}


result = ''# Results will temporarily hold either the string conversion to either the encrypted or decrypted string.
message = ''# Message temporarily holds the user's imputed string to be encrypted or decrypted.
choice = ''# Choice holds the users string input.

"""  The brain of my encrypter/decrypter it is a while statement running until the choice variable is equal to
-1. It holds three if/elif/else statements to make decisions on user imputed choice strings. """
while choice != '-1':
    choice = input("\nDo you want to ecrypt or decrypt the message?\nEnter 1 to Encrypt, 2 to Decrypt, -1 to Exit program: ")# Puts the users input into choice.

    """ The first flow statement checks if choice is equal to 1. If it does it asks the user
    to input their message to be encrypted then encrypts the message and prints the encrypted
    message to the user. Last we reset all of our variables. The second flow statement checks
    if choice is equal to 2. If it does it asks the user to input their message to be decrypted
    then decrypts the string and prints the message to the user. Last it resets all our variables.
    The last flow statement catches all non accepted choice inputs and allerts the user to re-enter """
    if choice == '1':
        message = input("\nEnter the message to encrypt: ")
        for i in range(0, len(message)):
            temp = message[i]
            for key in lib.keys():
                if key is temp:
                    result = result + str(lib[key])
        print(result + " Remember to copy this encryption to paste to be decrypted.(:")
        result, message = '';

    elif choice == '2':
        message = input("\nEnter the message to decrypt: ")
        for i, j in zip(message[::2], message[1::2]):
            temp = (i + j)
            for key in lib:
                value = lib[key]
                if temp == value:
                    result = result + key
        print(result)
        result, message = ''

    elif choice != '-1':
        print("You have entered an invalid choice. Please try again.")