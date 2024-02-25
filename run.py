""" desktop-app-template in Python3 using Tkinter """

# imports
from tkinter import Tk

from lib.app_root import *
from lib.components import *
from lib.functions import *

# creating root
root = Tk()
root.title('MyApp')
root.iconbitmap('resources/favicon.ico')
root.geometry(generate_tk_geometry(root, user_preferences['width'], user_preferences['height']))
root.configure(bg=generate_grayscale_hex(20))

# creating StartPage instance 'startPage'
startPage = StartPage(root)


def raiseStart(*args):
    root.geometry(generate_tk_geometry(root, user_preferences['width'], user_preferences['height']))
    startPage.mainFrame.tkraise()


raiseStart()

# binds
root.bind('<Control-q>', program_quit)
root.bind('<Control-r>', program_restart)
root.bind('<Escape>', raiseStart)
root.bind('<Button-4>', raiseStart)

# mainloop
root.mainloop()


