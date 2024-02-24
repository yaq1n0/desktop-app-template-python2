# template for Python Desktop App using Tkinter

from os import execv
from sys import executable, argv
# imports
from tkinter import Tk

from lib.components import *
from lib.functions import generate_grayscale_hex, generate_tk_geometry
from lib.app_root import user_preferences


# functions
def programRestart(*args):
    if user_preferences['dev']:
        print('[program] restart')

    # code from 'https://blog.petrzemek.net/2014/03/23/restarting-a-python-script-within-itself/'
    execv(executable, ['python'] + argv)

    return None


def programQuit(*args):
    if user_preferences['dev']:
        print('[program] quit')

    exit()

    return None


# creating root
root = Tk()
root.title('MyApp')
root.iconbitmap('resources/favicon.ico')
root.resizable(False, False)
root.geometry(generate_tk_geometry(root, user_preferences['width'], user_preferences['height']))
root.configure(bg=generate_grayscale_hex(20))

# creating StartPage instance 'startPage'
startPage = StartPage(root)


def raiseStart(*args):
    root.geometry(generate_tk_geometry(root, int(user_preferences['height'] / 2), user_preferences['height']))
    startPage.mainFrame.tkraise()


raiseStart()

# binds
root.bind('<Control-q>', programQuit)
root.bind('<Control-r>', programRestart)
root.bind('<Escape>', raiseStart)

# mainloop
root.mainloop()
