""" function to restart the program """

# imports
from os import execv
from sys import executable, argv

<<<<<<< Updated upstream:lib/functions/program_restart.py
=======
from lib.preferences import *
from tkinter import Tk

>>>>>>> Stashed changes:lib/core/program_restart.py

def program_restart(*args):
    """ code from 'https://bobbyhadz.com/blog/how-to-restart-python-script-from-within-itself' """
    execv(executable, ['python3'] + argv)
