# MyButton Class

# imports
from tkinter import Button, RIDGE

from lib.app_root import *
from lib.functions import *


class AppButton(Button):
    bgcolor, fgcolor, relwidth, relheight = generate_grayscale_hex(40), generate_grayscale_hex(220), 0.10, 0.05
    abgcolor, afgcolor = bgcolor, fgcolor

    def __init__(self, parent, text, command, relx, rely):
        self.text, self.command, self.relx, self.rely = text, command, relx, rely

        Button.__init__(self, parent)

        self.configure_()
        self.place_()

    def configure_(self):
        self.configure(text=self.text, command=self.command,
                       font=fonts['DefaultBold'],
                       bg=self.bgcolor, fg=self.fgcolor,
                       activebackground=self.abgcolor, activeforeground=self.afgcolor,
                       relief=RIDGE, highlightthickness=0, bd=0)

    def place_(self):
        self.place(relx=self.relx, rely=self.rely, relwidth=self.relwidth, relheight=self.relheight)
