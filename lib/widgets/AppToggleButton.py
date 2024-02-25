""" AppToggleButton class"""

from lib.app_root import generate_fonts
from lib.functions import generate_grayscale_hex
from .AppButton import AppButton
from .AppFrame import AppFrame
from .AppLabel import AppLabel


class AppToggleButton(object):
    """ AppToggleButton class """
    relwidth, relheight, enabled = 0.20, 0.10, False

    def __init__(self, parent, text, relx, rely):
        self.parent, self.text, self.relx, self.rely = parent, text, relx, rely
        self.defaults()

    def defaults(self):
        self.createTitleLabel()
        self.createFrames()

    def createTitleLabel(self):
        self.titleLabel = AppLabel(self.parent, self.text, self.relx, self.rely - 0.05)
        self.titleLabel.configure(font=generate_fonts()['LargeBold'])

    def createFrames(self):
        self.mainFrame = AppFrame(self.parent, generate_grayscale_hex(0))
        self.mainFrame.place(relx=self.relx, rely=self.rely, relwidth=self.relwidth, relheight=self.relheight)

        self.frame1 = AppFrame(self.mainFrame, generate_grayscale_hex(80))
        self.frame2 = AppFrame(self.mainFrame, generate_grayscale_hex(60))

        self.button1 = AppButton(self.frame1, 'Disabled', self.func1, 0, 0)
        self.button2 = AppButton(self.frame2, 'Enabled', self.func2, 0, 0)

        gs20, gs40, gs180 = generate_grayscale_hex(20), generate_grayscale_hex(40), generate_grayscale_hex(180)
        self.button1.configure(bg=gs40, activebackground=gs180, fg=gs20)
        self.button2.configure(bg=gs180, activebackground=gs40, fg=gs20)

        self.button1.place(relwidth=1, relheight=1)
        self.button2.place(relwidth=1, relheight=1)

    def func1(self):
        self.frame2.tkraise()
        self.enabled = True

    def func2(self):
        self.frame1.tkraise()
        self.enabled = False
