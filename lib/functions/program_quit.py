""" function to quit the program """

# imports
from lib.app_root import *


def program_quit(*args):
    if user_preferences['dev']:
        print('[program] quit')

    exit()
