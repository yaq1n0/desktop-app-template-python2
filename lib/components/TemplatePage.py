# <template> page class

# imports

from lib.components import *
from lib.widgets import AppFrame, AppLabel
from lib.functions import generate_grayscale_hex
from lib.app_root import fonts


class TemplatePage(object):
    def __init__(self, root):
        self.root = root

        self.defaults()

    def defaults(self):
        self.createFrame()
        self.createTitle()

    def createFrame(self):
        self.mainFrame = AppFrame(self.root, generate_grayscale_hex(20))

    def createTitle(self):
        self.titleLabel = AppLabel(self.mainFrame, 'Template Page', 0.25, 0.10)
        self.titleLabel.configure(font=fonts['ExtraLargeBold'])
        self.titleLabel.place(relwidth=0.50)
