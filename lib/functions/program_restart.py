""" function to restart the program """

# imports
from os import execv
from sys import executable, argv


def program_restart(*args):
    """ code from 'https://bobbyhadz.com/blog/how-to-restart-python-script-from-within-itself' """
    execv(executable, ['python3'] + argv)
