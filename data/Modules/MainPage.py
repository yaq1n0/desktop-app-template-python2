# main page class

# imports
from data.MyClasses import MyFrame, MyLabel
from data.MyFunctions import GrayScale
from data.MyVariables import MyFonts


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
