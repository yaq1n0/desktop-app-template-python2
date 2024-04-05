""" desktop-app-template in Python3 using Tkinter """

from tkinter import Tk
from components import StartPage

# creating Tk root
root = Tk()
root.title('MyApp')
root.iconbitmap('resources/images/favicon.ico')
root.minsize(width=1280, height=720)

# creating StartPage instance 'startPage' and raising it
startPage = StartPage(root)


def raiseStart(event) -> None:
    startPage.mainFrame.tkraise()


raiseStart(None)

# binds
root.bind('<Escape>f', raiseStart)
root.bind('<Button-4>', raiseStart)

# mainloop
root.mainloop()
