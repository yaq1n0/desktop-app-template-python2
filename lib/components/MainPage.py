# main page class

from lib.vars import MyFonts

# imports
from lib.functions import GrayScale


class MainPage(object):
    def __init__(self, root):
        self.root = root

        self.defaults()

    def defaults(self):
        self.createFrame()
        self.createTitle()

    def createFrame(self):
        self.mainFrame = MyFrame(self.root, GrayScale(20))

    def createTitle(self):
        self.titleLabel = MyLabel(self.mainFrame, 'Main Page', 0.25, 0.10)
        self.titleLabel.configure(font=MyFonts['ExtraLargeBold'])
        self.titleLabel.place(relwidth=0.50)
