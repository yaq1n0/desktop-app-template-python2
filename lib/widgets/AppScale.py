""" AppScale class """

# imports
from tkinter import Scale, Label, StringVar, HORIZONTAL, RIDGE, FLAT

from lib.app_root import generate_fonts
from lib.functions import generate_grayscale_hex


class AppScale(Scale):
    """ AppScale class """
    bgcolor, fgcolor, lowrange, highrange, resolution, s_relwidth, s_relheight = (
        generate_grayscale_hex(20),
        generate_grayscale_hex(220), 1.0, 100.0, 0.1, 0.10, 0.05)

    def __init__(self, parent, text, relx, rely):
        self.parent, self.text, self.relx, self.rely = parent, text, relx, rely

        Scale.__init__(self, self.parent)

        self.l_val = StringVar()
        self.defaults()

    def defaults(self):
        self.scaleConfigure()
        self.scalePlace()
        self.createLabel()

    def scaleConfigure(self):
        self.configure(command=self.update,
                       from_=self.lowrange, to=self.highrange,
                       orient=HORIZONTAL, showvalue=False, resolution=self.resolution,
                       bg=self.bgcolor, fg=self.fgcolor,
                       relief=RIDGE, highlightthickness=0, bd=0)

    def scalePlace(self):
        self.place(relx=self.relx, rely=(self.rely + 0.01), relwidth=self.s_relwidth, relheight=self.s_relheight)

    def createLabel(self):
        self.label = Label(self.parent)

        self.labelConfigure()
        self.labelPlace()

    def labelConfigure(self):
        self.label.configure(textvariable=self.l_val,
                             font=generate_fonts()['Large'],
                             bg=self.bgcolor, fg=self.fgcolor,
                             relief=FLAT,
                             padx=2, pady=2)

    def labelPlace(self):
        self.label.place(relx=self.relx, rely=self.rely - 0.050)

    def update(self, *args):
        self.l_val.set(self.text + ' = ' + str(Scale.get(self)))
