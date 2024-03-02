""" desktop-app-template in Python3 using Tkinter """


from tkinter import Tk

<<<<<<< Updated upstream
from lib.AppState import AppState
from lib.functions import generate_tk_geometry, generate_grayscale_hex, program_quit, program_restart
from components import StartPage
=======
from lib.preferences import *
from components import *
from lib.functions import *
>>>>>>> Stashed changes


# loading AppState
user_preferences_dict = AppState().user_preferences.asDict()

# creating Tk root
root = Tk()
root.title('MyApp')
<<<<<<< Updated upstream
root.iconbitmap('resources/favicon.ico')
root.geometry(generate_tk_geometry(root, user_preferences_dict['width'], user_preferences_dict['height']))
=======
root.iconbitmap('resources/images/favicon.ico')
root.geometry(generate_tk_geometry(root, user_preferences['width'], user_preferences['height']))
>>>>>>> Stashed changes
root.configure(bg=generate_grayscale_hex(20))

# creating StartPage instance 'startPage' and raising it
startPage = StartPage(root)


def raiseStart():
    startPage.mainFrame.tkraise()


raiseStart()

# binds
root.bind('<Control-q>', program_quit)
root.bind('<Control-r>', program_restart)
root.bind('<Escape>', raiseStart)
root.bind('<Button-4>', raiseStart)

# mainloop
root.mainloop()
