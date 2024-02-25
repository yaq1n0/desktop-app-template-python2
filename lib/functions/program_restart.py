""" function to restart the program """
import sys
# imports
from os import execv
from sys import executable, argv

from lib.app_root import *
from tkinter import Tk


def program_restart(*args):
    if user_preferences['dev']:
        print('[program] restart')

    """ code from 'https://bobbyhadz.com/blog/how-to-restart-python-script-from-within-itself' """
    execv(executable, ['python3'] + argv)
