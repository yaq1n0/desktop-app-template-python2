""" DemoPage class """

from main import appState
from lib.functions import generate_grayscale_hex
from lib.widgets import AppFrame, AppLabel


class DemoPage(object):
    """ DemoPage class """

    def __init__(self, root):
        self.root = root

        self.createFrame()
        self.createTitle()

    def createFrame(self):
        self.mainFrame = AppFrame(self.root, generate_grayscale_hex(20))

    def createTitle(self):
        self.titleLabel = AppLabel(self.mainFrame, 'Demo Page', 0.25, 0.10)
        self.titleLabel.configure(font=appState.fonts['ExtraLargeBold'])
        self.titleLabel.place(relwidth=0.50)
