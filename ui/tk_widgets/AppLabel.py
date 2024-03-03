""" AppLabel class """

# imports
from tkinter import Label, FLAT, N

from core import generate_grayscale_hex, load_fonts


class AppLabel(Label):
    """ AppLabel class """
    bgcolor, fgcolor = generate_grayscale_hex(20), generate_grayscale_hex(220)

    def __init__(self, parent, text, relx, rely):
        self.parent, self.text, self.relx, self.rely = parent, text, relx, rely

        Label.__init__(self, self.parent)

        self.configure_()
        self.place_()

    def configure_(self):
        self.configure(text=self.text,
                       font=load_fonts()['Default'],
                       bg=self.bgcolor, fg=self.fgcolor,
                       relief=FLAT, anchor=N,
                       padx=2, pady=2)

    def place_(self):
        self.place(relx=self.relx, rely=self.rely)
