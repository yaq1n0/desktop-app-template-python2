""" MainPage class """

from lib.app_root import *
from lib.functions import *
from lib.widgets import *


class MainPage(object):
    """ MainPage class """

    def __init__(self, root):
        self.root = root

        self.createFrame()
        self.createTitle()

    def createFrame(self):
        self.mainFrame = AppFrame(self.root, generate_grayscale_hex(20))

    def createTitle(self):
        self.titleLabel = AppLabel(self.mainFrame, 'Main Page', 0.25, 0.10)
        self.titleLabel.configure(font=fonts['ExtraLargeBold'])
        self.titleLabel.place(relwidth=0.50)
